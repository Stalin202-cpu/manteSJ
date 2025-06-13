# C:\proyectos-django\laboratorioSJ\Aplicaciones\pruebaLaboratorio\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('inicio',views.inicio,name='inicio'),
    path('nuevaZona', views.nuevaZona),  # corregido
    path('guardarZona', views.guardarZona),  # corregido
    path('eliminarZona/<id>', views.eliminarZona),  # corregido
    path('editarZona/<id>',views.editarZona),
    path('procesarEdicionZonas', views.procesarEdicionZonas)
]
