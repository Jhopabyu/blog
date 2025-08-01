from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Login(request):
    return HttpResponse("Esta es la vista de Login")

def Register(request):
    return HttpResponse("Esta es la vista de Register")