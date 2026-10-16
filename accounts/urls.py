from django.urls import path
from .views import OnboardingView, PerfilView, LocalDevLoginView

app_name = 'accounts'

urlpatterns = [
    path('onboarding/', OnboardingView.as_view(), name='onboarding'),
    path('perfil/', PerfilView.as_view(), name='perfil'),
    path('local-login/', LocalDevLoginView.as_view(), name='local_login'),
]
