from django.contrib import admin
from .models import ProgresoTarjeta, SesionEstudio


@admin.register(ProgresoTarjeta)
class ProgresoTarjetaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tarjeta', 'estado', 'intervalo_dias', 'aciertos', 'fallos', 'proxima_revision')
    list_filter = ('estado', 'intervalo_dias', 'proxima_revision')
    search_fields = ('usuario__username', 'tarjeta__pregunta')


@admin.register(SesionEstudio)
class SesionEstudioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'duracion_minutos', 'tarjetas_estudiadas', 'preguntas_respondidas', 'aciertos_test', 'fallos_test', 'fecha_inicio', 'completada')
    list_filter = ('duracion_minutos', 'completada', 'fecha_inicio')
    search_fields = ('usuario__username',)
