from django.urls import path
from . import views
from.views import organizacion,crear_organizacion  



urlpatterns = [
    path('organizacion/',views.organizacion,name='organizacion'),
    path('crear/',views.crear_organizacion,name='crear_organizacion'),
    
]