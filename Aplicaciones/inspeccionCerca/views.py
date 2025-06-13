from .models import zonaSeguridad
from .models import inspeccionCerca
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
import os


def inicio2(request):
    listadoInspeccion = inspeccionCerca.objects.all()
    return render(request, "inicio2.html", {'Cercas': listadoInspeccion})
# Renderizar el formulario para nueva prueba

def nuevaInspecion(request):
    remZonas=zonaSeguridad.objects.all()
    return render(request, "nuevaInspeccion.html",{'zonas':remZonas})

# Función encargada de guardar una nueva prueba en la base de datos
def guardarInspeccion(request):

    inspector = request.POST["inspector"]
    estado = request.POST["estado"]
    fecha = request.POST["fecha"]

    inspeccionId = request.POST["zona"]
    zona=zonaSeguridad.objects.get(id=inspeccionId)

    pdf=request.FILES.get("pdf")


    inspeccionCerca.objects.create(zona=zona, inspector=inspector, estado=estado, fecha=fecha, pdf=pdf)

    #Mensaje de confirmacion 
    messages.success(request, "La Inspeccion de la Serca guardado exitosamente")
    return redirect('inicio2')

# Eliminar una prueba por ID
def eliminarInspeccion(request, id):
    facturaEliminar = inspeccionCerca.objects.get(id=id)
    

    if facturaEliminar.pdf and os.path.isfile(os.path.join(settings.MEDIA_ROOT, facturaEliminar.pdf.name)):
        os.remove(os.path.join(settings.MEDIA_ROOT, facturaEliminar.pdf.name))
    
    facturaEliminar.delete()
    return redirect('inicio2')

# Mostrando formulario de ediccion
def editarInspeccion(request, id):

    inspeccionEditar = inspeccionCerca.objects.get(id=id)
    remZonas=zonaSeguridad.objects.all()

    return render(request, "editarIncpeccion.html", {'inspeccionEditar': inspeccionEditar, 'zonas':remZonas})

def procesarEdicionInspeccion(request):
    
    id=request.POST["id"]

    inspeccionId = request.POST["zona"]
    zona=zonaSeguridad.objects.get(id=inspeccionId)
    inspector = request.POST["inspector"]
    estado = request.POST["estado"]
    fecha = request.POST["fecha"]

    pdf=request.FILES.get("pdf")


    
    inspeccion2=inspeccionCerca.objects.get(id=id)
    inspeccion2.zona=zona
    inspeccion2.inspector=inspector
    inspeccion2.estado=estado
    inspeccion2.fecha=fecha

    if pdf:
        if inspeccion2.pdf:
            rutaPdf = os.path.join(settings.MEDIA_ROOT, str(inspeccion2.pdf))
            if os.path.isfile(rutaPdf):
                os.remove(rutaPdf)
        inspeccion2.pdf = pdf
        


    inspeccion2.save()
    #Mensaje de confirmacion
    messages.success(request, "Inspeccion de la Cerca Actualizado exitosamente")
    return redirect('inicio2')


