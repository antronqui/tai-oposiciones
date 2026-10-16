from django.urls import path
from .views import ExamenesListView, ExamenDetailView

app_name = 'examenes'

urlpatterns = [
    path('', ExamenesListView.as_view(), name='lista'),
    path('<int:pk>/', ExamenDetailView.as_view(), name='detalle'),
]
