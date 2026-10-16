from django.contrib import admin
from .models import Tarjeta


@admin.register(Tarjeta)
class TarjetaAdmin(admin.ModelAdmin):
    list_display = ('id', 'tema', 'tipo', 'pregunta_corta', 'nivel_dificultad', 'fuente', 'activa')
    list_filter = ('tipo', 'nivel_dificultad', 'tema__bloque', 'tema', 'activa')
    search_fields = ('pregunta', 'respuesta', 'explicacion', 'fuente')
    list_editable = ('activa', 'nivel_dificultad')

    def pregunta_corta(self, obj):
        return obj.pregunta[:50] + ("..." if len(obj.pregunta) > 50 else "")
    pregunta_corta.short_description = "Pregunta"
