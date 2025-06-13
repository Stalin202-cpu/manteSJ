from django.db import models
from Aplicaciones.zonaSeguridad.models import zonaSeguridad

class inspeccionCerca(models.Model):
    id = models.AutoField(primary_key=True)
    zona = models.ForeignKey(zonaSeguridad, on_delete=models.CASCADE)
    inspector = models.CharField(max_length=100)
    fecha = models.DateField()
    estado = models.CharField()
    pdf=models.FileField(upload_to='pdf', null=True, blank=True)

    def __str__(self): 
        fila = "{0}:  {1}  {2}   {3}"
        return fila.format(self.id, self.fecha, self.monto, self.productos)
