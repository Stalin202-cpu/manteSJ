from django.db import models
from Aplicaciones.inspeccionCerca.models import inspeccionCerca

class repacionCerca(models.Model):
    id = models.AutoField(primary_key=True)
    cerca = models.ForeignKey(inspeccionCerca, on_delete=models.CASCADE)
    equipo = models.CharField(max_length=100)
    fecha= models.DateField()
    materiales = models.CharField()
    logo=models.FileField(upload_to='cargos', null=True, blank=True)

    def __str__(self): 
        fila = "{0}:  {1}  {2}   {3}"
        return fila.format(self.id, self.fecha, self.monto, self.productos)