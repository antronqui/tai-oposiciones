from django import forms
from .models import UserProfile


class OnboardingForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['horas_semanales', 'nivel_previo', 'fecha_objetivo']
        widgets = {
            'horas_semanales': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 60, 'placeholder': 'Ej. 10'}),
            'nivel_previo': forms.Select(attrs={'class': 'form-select'}),
            'fecha_objetivo': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'horas_semanales': 'Horas semanales disponibles para estudiar',
            'nivel_previo': 'Nivel de partida',
            'fecha_objetivo': 'Fecha estimada de examen / objetivo TAI',
        }
        help_texts = {
            'horas_semanales': 'Calcularemos tu ritmo diario de repaso y nuevas tarjetas según tu disponibilidad.',
            'fecha_objetivo': 'Si no lo tienes claro, puedes seleccionar una fecha orientativa para 2027.',
        }
