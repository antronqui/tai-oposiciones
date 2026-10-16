from django.contrib import admin
from .models import Examen, PreguntaExamen


class PreguntaExamenInline(admin.StackedInline):
    model = PreguntaExamen
    extra = 1
    fields = ('numero', 'pregunta', ('opcion_a', 'opcion_b'), ('opcion_c', 'opcion_d'), ('opcion_correcta', 'tema', 'anulada'), 'explicacion_oficial')


@admin.register(Examen)
class ExamenAdmin(admin.ModelAdmin):
    list_display = ('año', 'convocatoria', 'tipo', 'organismo', 'total_preguntas')
    list_filter = ('año', 'convocatoria')
    search_fields = ('año', 'descripcion')
    inlines = [PreguntaExamenInline]

    def total_preguntas(self, obj):
        return obj.preguntas.count()
    total_preguntas.short_description = "Nº Preguntas"


@admin.register(PreguntaExamen)
class PreguntaExamenAdmin(admin.ModelAdmin):
    list_display = ('examen', 'numero', 'pregunta_corta', 'opcion_correcta', 'tema', 'anulada')
    list_filter = ('examen__año', 'opcion_correcta', 'tema__bloque', 'tema', 'anulada')
    search_fields = ('pregunta', 'explicacion_oficial', 'opcion_a', 'opcion_b', 'opcion_c', 'opcion_d')

    def pregunta_corta(self, obj):
        return obj.pregunta[:60] + ("..." if len(obj.pregunta) > 60 else "")
    pregunta_corta.short_description = "Enunciado"
