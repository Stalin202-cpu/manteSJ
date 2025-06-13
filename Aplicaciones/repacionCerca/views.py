from .models import repacionCerca
from .models import inspeccionCerca
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
import os


def inicio3(request):
    listadoReparacion = inspeccionCerca.objects.all()
    return render(request, "inicio3.html", {'Repacion': listadoReparacion})
# Renderizar el formulario para nueva prueba

def nuevaReparacion(request):
    remCercas=repacionCerca.objects.all()
    return render(request, "nuevaReparacion.html",{'cercas':remCercas})

# Función encargada de guardar una nueva prueba en la base de datos
def guardarReparacion(request):

    equipo = request.POST["equipo"]
    fecha1 = request.POST["fecha1"]
    materiales = request.POST["materiales"]

    reparacionId = request.POST["cerca"]
    cerca=repacionCerca.objects.get(id=reparacionId)

    logo1=request.FILES.get("logo1")


    inspeccionCerca.objects.create(equipo=equipo, fecha1=fecha1, materiales=materiales, cerca=cerca, logo1=logo1)

    #Mensaje de confirmacion 
    messages.success(request, "La Reparacion de la Serca guardado exitosamente")
    return redirect('inicio3')

# Eliminar una prueba por ID
def eliminarReparacion(request, id):
    repacionEliminar = inspeccionCerca.objects.get(id=id)

    if repacionEliminar.logo1 and os.path.isfile(os.path.join(settings.MEDIA_ROOT, repacionEliminar.logo1.name)):
        os.remove(os.path.join(settings.MEDIA_ROOT, repacionEliminar.logo1.name))
    
    repacionEliminar.delete()
    return redirect('inicio3')

# Mostrando formulario de ediccion
def editarReparacion(request, id):

    reparacionEditar = inspeccionCerca.objects.get(id=id)
    remRepa=repacionCerca.objects.all()

    return render(request, "editarIncpeccion.html", {'reparacionEditar': reparacionEditar, 'cercas':remRepa})

def procesarEdicionReparacion(request):
    
    id=request.POST["id"]

    reparacionId = request.POST["cerca"]
    cerca=repacionCerca.objects.get(id=reparacionId)

    equipo = request.POST["equipo"]
    fecha1 = request.POST["fecha1"]
    materiales = request.POST["materiales"]

    logo1=request.FILES.get("logo1")


    
    reparacion2=repacionCerca.objects.get(id=id)
    reparacion2.cerca=cerca
    reparacion2.equipo=equipo
    reparacion2.fecha1=fecha1
    reparacion2.materiales=materiales

    if logo1 :
        if reparacion2.logo1:
            rutaLogo = os.path.join(settings.MEDIA_ROOT, str(reparacion2.logo1))
            if os.path.isfile(rutaLogo):
                os.remove(rutaLogo)
        reparacion2.logo1 = logo1
        


    reparacion2.save()
    #Mensaje de confirmacion
    messages.success(request, "Inspeccion de la Cerca Actualizado exitosamente")
    return redirect('inicio3')


