from django.shortcuts import render, redirect
from .models import zonaSeguridad
from django.contrib import messages
from django.conf import settings
import os

def inicio(request):
    listadoZona = zonaSeguridad.objects.all()
    return render(request, "inicio.html", {'Seguridad': listadoZona})

# Renderizar el formulario para nueva prueba
def nuevaZona(request):
    return render(request, "nuevaZona.html")

# Función encargada de guardar una nueva prueba en la base de datos
def guardarZona(request):
    nombre = request.POST["nombre"]
    tipoCerca = request.POST["tipoCerca"]
    longitud = request.POST["longitud"]

    #Subiendo archivo con parentecis
    logo=request.FILES.get("logo")

    zonaSeguridad.objects.create(nombre=nombre, tipoCerca=tipoCerca, longitud=longitud, logo=logo)

    #Mensaje de confirmacion 
    messages.success(request, "Zona de Seguridad guardado exitosamente")
    return redirect('inicio')

# Eliminar una prueba por ID
def eliminarZona(request, id):
    zonaEliminar = zonaSeguridad.objects.get(id=id)

    if zonaEliminar.logo and os.path.isfile(os.path.join(settings.MEDIA_ROOT, zonaEliminar.logo.name)):
        os.remove(os.path.join(settings.MEDIA_ROOT, zonaEliminar.logo.name))


    zonaEliminar.delete()
    return redirect('inicio')

# Mostrando formulario de ediccion
def editarZona(request, id):
    zonaEditar = zonaSeguridad.objects.get(id=id)
    return render(request, "editarZona.html", {'zonaEditar': zonaEditar})

def procesarEdicionZonas(request):
    
    id=request.POST["id"]
    nombre = request.POST["nombre"]
    tipoCerca = request.POST["tipoCerca"]
    longitud = request.POST["longitud"]
    logo=request.FILES.get("logo")
    
    zona2=zonaSeguridad.objects.get(id=id)
    zona2.nombre=nombre
    zona2.tipoCerca=tipoCerca
    zona2.longitud=longitud
    if logo :
        if zona2.logo:
            rutaLogo = os.path.join(settings.MEDIA_ROOT, str(zona2.logo))
            if os.path.isfile(rutaLogo):
                os.remove(rutaLogo)
        zona2.logo = logo
        
    zona2.save()
    #Mensaje de confirmacion
    messages.success(request, "Zona de Seguridad Actualizado exitosamente")
    return redirect('inicio')

