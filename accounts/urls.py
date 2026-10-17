from django.urls import path
from .views import (
    OnboardingView,
    PerfilView,
    LocalDevLoginView,
    GestionAccesosView,
    AprobarAccesoView,
    RechazarAccesoView,
    DesactivarAccesoView,
    InvitarUsuarioView
)

app_name = 'accounts'

urlpatterns = [
    path('onboarding/', OnboardingView.as_view(), name='onboarding'),
    path('perfil/', PerfilView.as_view(), name='perfil'),
    path('local-login/', LocalDevLoginView.as_view(), name='local_login'),
    
    # Gestión de accesos e invitaciones (Solo Administrador)
    path('gestion-accesos/', GestionAccesosView.as_view(), name='gestion_accesos'),
    path('gestion-accesos/aprobar/<int:pk>/', AprobarAccesoView.as_view(), name='aprobar_acceso'),
    path('gestion-accesos/rechazar/<int:pk>/', RechazarAccesoView.as_view(), name='rechazar_acceso'),
    path('gestion-accesos/desactivar/<int:pk>/', DesactivarAccesoView.as_view(), name='desactivar_acceso'),
    path('gestion-accesos/invitar/', InvitarUsuarioView.as_view(), name='invitar_usuario'),
]
