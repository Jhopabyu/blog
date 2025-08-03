from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from proyecto.models import Proyecto
from django.contrib.admin.views.decorators import staff_member_required
from .forms import ProyectoForm

# Create your views here.
PROVINCIAS_EC=[
    {"id":1,"name":"Azuay"},
    {"id":2,"name":"Bolivar"},
    {"id":3,"name":"Canar"},
    {"id":4,"name":"Carchi"},
    {"id":5,"name":"Cotopaxi"},
    {"id":6,"name":"Chimborazo"},
    {"id":7,"name":"El Oro"},
    {"id":8,"name":"Esmeraldas"},
    {"id":9,"name":"Guayas"},
    {"id":10,"name":"Imbabura"},
    {"id":11,"name":"Loja"},
    {"id":12,"name":"Los Rios"},
    {"id":13,"name":"Manabi"},
    {"id":14,"name":"Miranda"},
    {"id":15,"name":"Nueva Esparta"},
    {"id":16,"name":"Pichincha"},
    {"id":17,"name":"Santa Elena"},
    {"id":18,"name":"Santo Domingo"},
    {"id":19,"name":"Sucumbios"},
    {"id":20,"name":"Tungurahua"},
    {"id":21,"name":"Zamora Chinchipe"}
]

def provincias_api(request):
    return JsonResponse(PROVINCIAS_EC, safe=False)



def proyectos_view(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyecto/proyectos.html')  # asegúrate de tener este template


#para solo registrar proyetos el admin  
@staff_member_required
def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proyectos')
    else:
        form = ProyectoForm()
    return render(request, 'proyecto/crear_proyecto.html', {'form': form})
