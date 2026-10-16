from django.urls import path
from .views import TemarioListView, TemaDetailView

app_name = 'temario'

urlpatterns = [
    path('', TemarioListView.as_view(), name='lista'),
    path('tema/<int:pk>/', TemaDetailView.as_view(), name='tema_detalle'),
]
