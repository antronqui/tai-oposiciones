from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Examen, PreguntaExamen


class ExamenesListView(LoginRequiredMixin, ListView):
    model = Examen
    template_name = "examenes/examenes_list.html"
    context_object_name = "examenes"

    def get_queryset(self):
        return Examen.objects.all().prefetch_related('preguntas')


class ExamenDetailView(LoginRequiredMixin, DetailView):
    model = Examen
    template_name = "examenes/examen_detail.html"
    context_object_name = "examen"
