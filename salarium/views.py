from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from globales.models import Provincias,Localidades,Empresas
from static import FuncionesGlobales

# Create your views here.
@login_required()

def HomeView(request): 
    empresa = Empresas.objects.raw("SELECT empresas.* FROM empresas")
    context= {
        'emp' : empresa,
    }
    return render(request,'index.html',context)
    #return render(request,'index.html')

def cerrarSesion(request):
    logout(request)
    return redirect('index')