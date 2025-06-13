# C:\proyectos-django\laboratorioSJ\Aplicaciones\pruebaLaboratorio\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('inicio2',views.inicio2,name='inicio2'),
    path('nuevaInspecion', views.nuevaInspecion),  # corregido
    path('guardarInspeccion', views.guardarInspeccion),  # corregido
    path('eliminarInspeccion/<id>', views.eliminarInspeccion),  # corregido
    path('editarInspeccion/<id>',views.editarInspeccion),
    path('procesarEdicionInspeccion', views.procesarEdicionInspeccion)
]
