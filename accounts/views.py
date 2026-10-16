from django.shortcuts import render, redirect
from django.views.generic import FormView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from .models import UserProfile, Invitacion
from .forms import OnboardingForm


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


class LocalDevLoginView(TemplateView):
    """
    Vista auxiliar para pruebas directas en desarrollo local
    """
    template_name = "accounts/local_login.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email', '').strip().lower()
        if not email:
            messages.error(request, "Introduce una dirección de correo válida.")
            return self.get(request, *args, **kwargs)

        # Comprobar invitación o crear si es admin
        es_invitado = Invitacion.objects.filter(email__iexact=email, activo=True).exists()
        user = User.objects.filter(email__iexact=email).first()

        if not user:
            if not es_invitado and email != "admin@tai.es":
                messages.error(request, f"El correo '{email}' no cuenta con una invitación activa.")
                return self.get(request, *args, **kwargs)
            
            # Crear usuario local
            username = email.split('@')[0]
            user = User.objects.create_user(username=username, email=email)
            if not es_invitado:
                Invitacion.objects.create(email=email, activo=True, comentario="Auto-invitación dev")

        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        messages.success(request, f"¡Bienvenido/a, {user.username}!")
        return redirect('dashboard')
