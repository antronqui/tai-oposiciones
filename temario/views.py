from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Bloque, Tema
from estudio.models import ProgresoPregunta


class TemarioListView(LoginRequiredMixin, ListView):
    model = Bloque
    template_name = "temario/bloques_list.html"
    context_object_name = "bloques"

    def get_queryset(self):
        return Bloque.objects.all().prefetch_related('temas__subtemas__conceptos', 'temas__tarjetas')


class TemaDetailView(LoginRequiredMixin, DetailView):
    model = Tema
    template_name = "temario/tema_detail.html"
    context_object_name = "tema"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tema = self.get_object()
        user = self.request.user
        context['subtemas'] = tema.subtemas.prefetch_related('conceptos')
        context['tarjetas'] = tema.tarjetas.filter(activa=True)
        context['preguntas_examen'] = tema.preguntas_examen.filter(anulada=False)
        context['total_preguntas'] = context['preguntas_examen'].count()
        context['falladas_count'] = ProgresoPregunta.objects.filter(
            usuario=user,
            pregunta__tema=tema,
            en_repaso_fallos=True
        ).count()
        return context

