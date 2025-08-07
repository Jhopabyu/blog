from django.shortcuts import render,redirect
from .models import Directivo
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import DirectivoForm

from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.
def organizacion(request):
    presidente = Directivo.objects.filter(cargo__icontains="Presidente").first()
    directivos = Directivo.objects.exclude(id=presidente.id) if presidente else Directivo.objects.all()
    return render(request, 'organizacion/organizacion.html',{'presidente':presidente, 'directivos':directivos})

@staff_member_required
def crear_organizacion(request):
    if request.method == 'POST':
        form = DirectivoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('organizacion')
    else:
        form = DirectivoForm()
    return render(request, 'organizacion/crear_organizacion.html', {'form': form})


