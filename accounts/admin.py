from django.contrib import admin
from .models import Invitacion, UserProfile


@admin.register(Invitacion)
class InvitacionAdmin(admin.ModelAdmin):
    list_display = ('email', 'nombre', 'activo', 'fecha_alta', 'comentario')
    list_filter = ('activo', 'fecha_alta')
    search_fields = ('email', 'nombre', 'comentario')
    list_editable = ('activo',)
    actions = ['aprobar_accesos', 'desactivar_accesos']

    @admin.action(description="Aprobar / Activar accesos seleccionados")
    def aprobar_accesos(self, request, queryset):
        count = queryset.update(activo=True)
        self.message_user(request, f"{count} accesos aprobados correctamente.")

    @admin.action(description="Desactivar / Revocar accesos seleccionados")
    def desactivar_accesos(self, request, queryset):
        count = queryset.update(activo=False)
        self.message_user(request, f"{count} accesos desactivados.")


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'horas_semanales', 'nivel_previo', 'fecha_objetivo', 'onboarding_completado', 'fecha_alta')
    list_filter = ('nivel_previo', 'onboarding_completado')
    search_fields = ('user__username', 'user__email')
