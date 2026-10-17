from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import FormView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from .models import UserProfile, Invitacion
from .forms import OnboardingForm


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_staff or self.request.user.is_superuser)

    def handle_no_permission(self):
        messages.error(self.request, "Acceso restringido a administradores.")
        return redirect('dashboard')


class OnboardingView(LoginRequiredMixin, FormView):
    template_name = "accounts/onboarding.html"
    form_class = OnboardingForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        profile, _ = UserProfile.objects.get_or_create(user=self.request.user)
        kwargs['instance'] = profile
        return kwargs

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.onboarding_completado = True
        profile.save()
        messages.success(self.request, "¡Tu plan de estudio personalizado ha sido configurado!")
        return super().form_valid(form)


class PerfilView(LoginRequiredMixin, UpdateView):
    template_name = "accounts/perfil.html"
    form_class = OnboardingForm
    success_url = reverse_lazy('accounts:perfil')

    def get_object(self, queryset=None):
        profile, _ = UserProfile.objects.get_or_create(user=self.request.user)
        return profile

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Perfil de estudio actualizado correctamente.")
        return super().form_valid(form)


class GestionAccesosView(StaffRequiredMixin, TemplateView):
    """
    Panel optimizado para móvil (iPhone) y escritorio:
    - Revisar y autorizar solicitudes pendientes de Google Login con un solo clic.
    - Invitar previamente a nuevos opositores por correo.
    - Gestionar y suspender/desactivar accesos autorizados.
    """
    template_name = "accounts/gestion_accesos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        admin_email = getattr(settings, 'ADMIN_EMAIL', 'antronqui@gmail.com').lower().strip()
        context['admin_email'] = admin_email
        context['pendientes'] = Invitacion.objects.filter(activo=False).order_by('-fecha_alta')
        context['autorizados'] = Invitacion.objects.filter(activo=True).order_by('-fecha_alta')
        return context


class AprobarAccesoView(StaffRequiredMixin, View):
    """
    Aprobar solicitud de acceso pendiente
    """
    def post(self, request, pk):
        inv = get_object_or_404(Invitacion, pk=pk)
        inv.activo = True
        inv.save()

        # Si ya existe el usuario creado en auth_user, activarlo
        User.objects.filter(email__iexact=inv.email).update(is_active=True)

        messages.success(request, f"¡Acceso aprobado para {inv.email}! Ya puede entrar con su cuenta de Google.")
        return redirect('accounts:gestion_accesos')


class RechazarAccesoView(StaffRequiredMixin, View):
    """
    Rechazar y eliminar solicitud de acceso
    """
    def post(self, request, pk):
        inv = get_object_or_404(Invitacion, pk=pk)
        admin_email = getattr(settings, 'ADMIN_EMAIL', 'antronqui@gmail.com').lower().strip()
        if inv.email.lower() == admin_email:
            messages.error(request, "No puedes eliminar la cuenta del administrador principal.")
            return redirect('accounts:gestion_accesos')

        email = inv.email
        inv.delete()
        messages.info(request, f"Solicitud de {email} eliminada.")
        return redirect('accounts:gestion_accesos')


class DesactivarAccesoView(StaffRequiredMixin, View):
    """
    Revocar / desactivar acceso a un usuario previamente autorizado
    """
    def post(self, request, pk):
        inv = get_object_or_404(Invitacion, pk=pk)
        admin_email = getattr(settings, 'ADMIN_EMAIL', 'antronqui@gmail.com').lower().strip()
        if inv.email.lower() == admin_email:
            messages.error(request, "No se puede revocar el acceso a la cuenta del administrador.")
            return redirect('accounts:gestion_accesos')

        inv.activo = False
        inv.save()
        User.objects.filter(email__iexact=inv.email).update(is_active=False)
        messages.warning(request, f"El acceso para {inv.email} ha sido revocado.")
        return redirect('accounts:gestion_accesos')


class InvitarUsuarioView(StaffRequiredMixin, View):
    """
    Invitar manualmente a un usuario añadiéndolo a la lista blanca autorizada
    """
    def post(self, request):
        email = request.POST.get('email', '').strip().lower()
        nombre = request.POST.get('nombre', '').strip()
        comentario = request.POST.get('comentario', '').strip() or "Invitado por el administrador"

        if not email or '@' not in email:
            messages.error(request, "Introduce una dirección de correo electrónico válida.")
            return redirect('accounts:gestion_accesos')

        inv, created = Invitacion.objects.update_or_create(
            email=email,
            defaults={
                'nombre': nombre,
                'activo': True,
                'comentario': comentario,
            }
        )

        User.objects.filter(email__iexact=email).update(is_active=True)

        if created:
            messages.success(request, f"¡Invitación autorizada para {email}! Ya puede iniciar sesión con Google.")
        else:
            messages.success(request, f"El usuario {email} ha sido reactivado / autorizado correctamente.")

        return redirect('accounts:gestion_accesos')


class LocalDevLoginView(TemplateView):
    """
    Vista auxiliar para pruebas directas en desarrollo local (restringida en producción)
    """
    template_name = "accounts/local_login.html"

    def get(self, request, *args, **kwargs):
        if not settings.DEBUG:
            messages.error(request, "El acceso directo local está deshabilitado en producción. Usa inicio de sesión con Google.")
            return redirect('landing')
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not settings.DEBUG:
            messages.error(request, "El acceso directo local está deshabilitado en producción.")
            return redirect('landing')

        email = request.POST.get('email', '').strip().lower()
        if not email:
            messages.error(request, "Introduce una dirección de correo válida.")
            return self.get(request, *args, **kwargs)

        admin_email = getattr(settings, 'ADMIN_EMAIL', 'antronqui@gmail.com').lower().strip()
        is_admin = (email == admin_email or email == "admin@tai.es")

        # Comprobar invitación o crear si es admin
        es_invitado = Invitacion.objects.filter(email__iexact=email, activo=True).exists()
        user = User.objects.filter(email__iexact=email).first()

        if not user:
            if not es_invitado and not is_admin:
                messages.error(request, f"El correo '{email}' no cuenta con una invitación activa.")
                return self.get(request, *args, **kwargs)
            
            # Crear usuario local
            username = email.split('@')[0]
            user = User.objects.create_user(
                username=username,
                email=email,
                is_superuser=is_admin,
                is_staff=is_admin
            )
            if not es_invitado:
                Invitacion.objects.create(
                    email=email,
                    nombre="Admin Dev" if is_admin else username,
                    activo=True,
                    comentario="Auto-invitación dev"
                )
        else:
            if is_admin and (not user.is_superuser or not user.is_staff):
                user.is_superuser = True
                user.is_staff = True
                user.save()

        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        messages.success(request, f"¡Bienvenido/a, {user.username}!")
        return redirect('dashboard')
