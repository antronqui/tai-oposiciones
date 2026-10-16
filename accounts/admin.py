from django.contrib import admin
from .models import Invitacion, UserProfile


@admin.register(Invitacion)
class InvitacionAdmin(admin.ModelAdmin):
    list_display = ('email', 'activo', 'fecha_alta', 'comentario')
    list_filter = ('activo', 'fecha_alta')
    search_fields = ('email', 'comentario')
    list_editable = ('activo',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'horas_semanales', 'nivel_previo', 'fecha_objetivo', 'onboarding_completado', 'fecha_alta')
    list_filter = ('nivel_previo', 'onboarding_completado')
    search_fields = ('user__username', 'user__email')
