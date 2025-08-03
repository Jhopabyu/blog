from django import forms
from .models import Proyecto

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'estado','provincia', 'pais', 'costo', 'equipo', 'f_aprobacion']
        widgets = {
            'f_aprobacion': forms.DateInput(attrs={'type': 'date'}),
            'f_actualizacion': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }