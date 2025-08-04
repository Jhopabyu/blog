from django.db import models
from django.http import HttpResponse

# Create your models here.

ESTADOS = [
        ('plan', 'Planificado'),
        ('ejec', 'En ejecución'),
        ('fin', 'Finalizado'),
    ]

class Proyecto(models.Model):
    nombre = models.CharField(max_length=255)
    estado = models.CharField(max_length=15,choices=ESTADOS, default='plan')
    pais = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100, null=True, blank=True)
    costo = models.DecimalField(max_digits=12, decimal_places=2)
    equipo = models.TextField(max_length=300)
    f_aprobacion = models.DateField()
    f_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} ({self.pais})"