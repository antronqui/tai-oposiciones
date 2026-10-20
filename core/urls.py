from django.urls import path
from .views import LandingView, DashboardView, healthz

urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('healthz/', healthz, name='healthz'),
]
