from django import forms
from .models import Proyecto

class ProyectoForm(forms.ModelForm):
    
    ESTADOS_CHOICES = [
        ('Planificado', 'Planificado'),
        ('En ejecución', 'En ejecución'),
        ('Finalizado', 'Finalizado'),
    ]
    
    nombre = forms.CharField(help_text= None,
                             label=False,
                             widget=forms.TextInput(attrs={'placeholder': 'Nombre del proyecto'}))
    estado = forms.ChoiceField(
        choices=ESTADOS_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'from-check-inline'}),
        label="Estado"
    )
    provincia = forms.CharField(label=False,
                                widget=forms.TextInput(attrs={'placeholder': 'Provincia'}))
    pais = forms.CharField(label=False,
                           widget=forms.TextInput(attrs={'placeholder': 'Pais'}))
    costo = forms.DecimalField(label=False,
                               widget=forms.NumberInput(attrs={'placeholder': 'Costo'}))
    equipo = forms.CharField(label=False,
                             widget=forms.Textarea(attrs={'placeholder': 'Equipo del proyecto'}))
    f_aprobacion = forms.DateField(label='Fecha de aprobación',
                                   widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Proyecto
        fields = ['nombre', 'estado','provincia', 'pais', 'costo', 'equipo', 'f_aprobacion']
        widgets = {
            'f_aprobacion': forms.DateInput(attrs={'type': 'date'}),
            'f_actualizacion': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }