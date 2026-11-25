
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Centro_costos
from globales.models import Provincias,Localidades, Empresas
from static import FuncionesGlobales

import datetime 
import decimal

def CentroCostosHomeView(request):

    provincias=Provincias.objects.raw("SELECT * FROM provincias ORDER BY nombre")
    localidades=Localidades.objects.raw("SELECT * FROM localidades")
    empresa=Empresas.objects.raw("SELECT * FROM empresas")
    centrocostos=Centro_costos.objects.raw("SELECT * FROM centrocostos")
    
    context={
        'centrocostos' : centrocostos,
        'emp' : empresa,
        'prov' : provincias,
        'localidades' : localidades,
    }
    return render(request,'centro_costos/index.html',context)
    
class CentroCostoView(View):
    def get(self,request,*args,**kwargs):
        provincias=Provincias.objects.raw("SELECT * FROM provincias ORDER BY nombre")
        localidades=Localidades.objects.raw("SELECT * FROM localidades")
        centrocostos=Centro_costos.objects.raw("SELECT * FROM centrocostos")
        empresa=Empresas.objects.raw("SELECT * FROM empresa")
        
        context={
            'Centro_Costos' : centrocostos,
            'emp' : empresa,
            'prov' : provincias,
            'localidades' : localidades,
        }
        return render(request,'centro_costos/centro_costos.html',context)
    
class AgregarCentroCosto(View):
        
    def post(self,request,*args,**kwargs):
        centrocostos=Centro_costos()
        centrocostos.id_empresa_id=request.POST.get('emp')  
        centrocostos.codigo=request.POST.get('codigo')
        centrocostos.nombre=request.POST.get('nombre').upper()
        centrocostos.domicilio=request.POST.get('domicilio').upper()
        centrocostos.provincia=request.POST.get('provincia')
        centrocostos.localidad=request.POST.get('localidad')
        
        centrocostos.save()
        return redirect('centrocostos:index')

def editarCentroCosto(request):
    id=request.POST.get('id')
    centrocostos=Centro_costos.objects.get(id=id) 

    centrocostos.codigo=request.POST.get('cod')
    centrocostos.nombre=request.POST.get('nom').upper()
    centrocostos.domicilio=request.POST.get('domicilio').upper()
    centrocostos.provincia=request.POST.get('provincia')
    centrocostos.localidad=request.POST.get('localidad')
    
    centrocostos.save()
            
    return redirect('centrocostos:index')

def eliminarCentroCosto(request):
    id=request.POST.get('id1')
    centrocostos=Centro_costos.objects.get(id=id)
    centrocostos.delete()
        
    return redirect('centrocostos:index')