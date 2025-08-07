from django import forms
from .models import Directivo

class DirectivoForm(forms.ModelForm):
    CARGO_CHOISES = [
        ('presidente', 'Presidente'),
        ('gerente', 'Gerente'),
        ('director', 'Director'),
        ('secretaria', 'Secretaria'),
        ('contador', 'Contador'),
    ]
    nombre = forms.CharField(help_text=None,
                             label=False,
                             widget=forms.TextInput(attrs={'placeholder': 'Nombre Completo'}))
    cargo = forms.ChoiceField(choices=CARGO_CHOISES,
                              widget=forms.Select(attrs={'class': 'form-select'}))
    biografia = forms.CharField(help_text=None,
                               label=False,
                               widget=forms.Textarea(attrs={'placeholder': 'Biografia'}))
    pais = forms.CharField(help_text=None,
                          label=False,
                          widget=forms.TextInput(attrs={'placeholder': 'Pais'}))
    foto = forms.ImageField(help_text=None,
                            label=False,
                            required=False,
                            widget=forms.FileInput())
    class Meta:
        model = Directivo
        fields = ['nombre', 
                  'cargo', 
                  'biografia', 
                  'pais', 
                  'foto']
        
