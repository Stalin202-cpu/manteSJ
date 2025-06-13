from django.db import models

# Create your models here.

from django.db import models

class zonaSeguridad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipoCerca = models.CharField(max_length=100)
    longitud = models.CharField(max_length=100)
    logo=models.FileField(upload_to='cargos', null=True, blank=True)

    def __str__(self): 
        fila = "{0}:  {1}  {2}   {3}"
        return fila.format(self.id, self.nombre, self.tipoCerca, self.longitud, self.logo )
