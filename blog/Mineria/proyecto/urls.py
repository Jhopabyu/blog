from django.urls import path
from .views import provincias_api, crear_proyecto
from . import views

urlpatterns = [
    path('api/provincias/', provincias_api, name='api_provincias'),
    path('listado/', views.proyectos_view, name='proyectos'),  # <-- esta es la ruta
    path('nuevo/', crear_proyecto, name='crear_proyecto'),

]
