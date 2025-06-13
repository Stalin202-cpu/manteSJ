# C:\proyectos-django\laboratorioSJ\Aplicaciones\pruebaLaboratorio\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('inicio3',views.inicio3,name='inicio3'),
    path('nuevaReparacion', views.nuevaReparacion),  # corregido
    path('guardarReparacion', views.guardarReparacion),  # corregido
    path('eliminarReparacion/<id>', views.eliminarReparacion),  # corregido
    path('editarReparacion/<id>',views.editarReparacion),
    path('procesarEdicionReparacion', views.procesarEdicionReparacion)
]
