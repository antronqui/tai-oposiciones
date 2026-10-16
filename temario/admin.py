from django.contrib import admin
from .models import Bloque, Tema, Subtema, Concepto


class SubtemaInline(admin.TabularInline):
    model = Subtema
    extra = 1


@admin.register(Bloque)
class BloqueAdmin(admin.ModelAdmin):
    list_display = ('numero', 'nombre', 'icono')
    ordering = ('numero',)


@admin.register(Tema)
class TemaAdmin(admin.ModelAdmin):
    list_display = ('bloque', 'numero', 'titulo', 'fuente_oficial', 'ultima_revision')
    list_filter = ('bloque', 'fuente_oficial')
    search_fields = ('titulo', 'descripcion', 'fuente_oficial')
    inlines = [SubtemaInline]


@admin.register(Subtema)
class SubtemaAdmin(admin.ModelAdmin):
    list_display = ('tema', 'titulo', 'orden')
    list_filter = ('tema__bloque', 'tema')
    search_fields = ('titulo',)


@admin.register(Concepto)
class ConceptoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtema', 'fuente_oficial')
    list_filter = ('subtema__tema__bloque', 'subtema__tema')
    search_fields = ('titulo', 'contenido')
