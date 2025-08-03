from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from proyecto.models import Proyecto
from django.contrib.admin.views.decorators import staff_member_required
from .forms import ProyectoForm

# Create your views here.
PROVINCIAS_EC = [
    {"id": 1, "name": "Azuay", "lat": -2.8975, "lng": -79.0045},
    {"id": 2, "name": "Bolivar", "lat": -1.6133, "lng": -79.0024},
    {"id": 3, "name": "Canar", "lat": -2.5521, "lng": -78.9389},
    {"id": 4, "name": "Carchi", "lat": 0.6167, "lng": -77.8333},
    {"id": 5, "name": "Cotopaxi", "lat": -0.9333, "lng": -78.6167},
    {"id": 6, "name": "Chimborazo", "lat": -1.6646, "lng": -78.6547},
    {"id": 7, "name": "El Oro", "lat": -3.2581, "lng": -79.9587},
    {"id": 8, "name": "Esmeraldas", "lat": 0.9682, "lng": -79.6517},
    {"id": 9, "name": "Guayas", "lat": -2.1709, "lng": -79.9224},
    {"id": 10, "name": "Imbabura", "lat": 0.3492, "lng": -78.1230},
    {"id": 11, "name": "Loja", "lat": -3.9931, "lng": -79.2042},
    {"id": 12, "name": "Los Rios", "lat": -1.15, "lng": -79.5},
    {"id": 13, "name": "Manabi", "lat": -0.9461, "lng": -80.7160},
    {"id": 14, "name": "Miranda", "lat": 10.4720, "lng": -66.5667},  # Venezuela
    {"id": 15, "name": "Nueva Esparta", "lat": 10.9605, "lng": -63.9101},
    {"id": 16, "name": "Pichincha", "lat": -0.1807, "lng": -78.4678},
    {"id": 17, "name": "Santa Elena", "lat": -2.2303, "lng": -80.8592},
    {"id": 18, "name": "Santo Domingo", "lat": -0.2545, "lng": -79.1717},
    {"id": 19, "name": "Sucumbios", "lat": 0.0881, "lng": -76.6610},
    {"id": 20, "name": "Tungurahua", "lat": -1.25, "lng": -78.6167},
    {"id": 21, "name": "Zamora Chinchipe", "lat": -4.0667, "lng": -78.9667},
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

def proyectos_por_provincia(request, provincia_id):
    provincia_nombre = next(
    (prov['name'] for prov in PROVINCIAS_EC if prov['id'] == provincia_id), None
    )
    if provincia_nombre is None:
        return JsonResponse({"error": "Provincia no válida"}, status=400)
    proyectos = Proyecto.objects.filter(provincia__iexact=provincia_nombre)  # filtro opcional
   
    data = [
        {
            'id': p.id,
            'nombre': p.nombre,
            'estado': p.estado,
            'pais': p.pais,
            'provincia': p.provincia,
            'costo': str(p.costo),
            'equipo': p.equipo,
            'f_aprobacion': p.f_aprobacion.strftime('%Y-%m-%d'),
            'f_actualizacion': p.f_actualizacion.strftime('%Y-%m-%d %H:%M:%S')
            
        }
        for p in proyectos
    ]
    return JsonResponse(data, safe=False)