from django.urls import path
from .views import (
    SeleccionarSesionView,
    IniciarSesionView,
    SesionFlashcardsView,
    RegistrarProgresoTarjetaAPI,
    TestAdaptativoView,
    FinalizarTestAPI
)

app_name = 'estudio'

urlpatterns = [
    path('seleccionar/', SeleccionarSesionView.as_view(), name='seleccionar_sesion'),
    path('iniciar/', IniciarSesionView.as_view(), name='iniciar_sesion'),
    path('flashcards/', SesionFlashcardsView.as_view(), name='sesion_flashcards'),
    path('api/tarjeta-progreso/', RegistrarProgresoTarjetaAPI.as_view(), name='api_tarjeta_progreso'),
    path('test/', TestAdaptativoView.as_view(), name='test_examen'),
    path('api/test-finalizar/', FinalizarTestAPI.as_view(), name='api_test_finalizar'),
]
