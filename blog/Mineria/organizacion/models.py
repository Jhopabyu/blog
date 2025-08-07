from django.db import models

# Create your models here.

class Directivo(models.Model):
    CARGOS=[
        ('presidente', 'Presidente'),
        ('gerente', 'Gerente'),
        ('director', 'Director'),
        ('secretaria', 'Secretaria'),
        ('contador', 'Contador'),
        ]
    nombre =models.CharField(max_length=50)
    cargo = models.CharField(max_length=50, choices=CARGOS)
    biografia = models.TextField()
    pais = models.CharField(max_length=50,blank=True)
    foto = models.ImageField(upload_to='directivos/',blank=True, null=True)
    fecha_ingreso = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.nombre} ({self.get_cargo_display()})'