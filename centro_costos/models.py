from django.db import models
from globales.models import Empresas

# Create your models here.
class Centro_costos(models.Model):

    nombre=models.CharField('Nombre de la Empresa',max_length=100,null=True, blank=True)
    domicilio=models.CharField('Domicilio',max_length=100,null=True, blank=True)
    id_empresa=models.ForeignKey('globales.Empresas',on_delete=models.CASCADE)
    
    def __str__(self):
        return '%s,%s,%s,%s' % (self.id, self.nombre, self.domicilio, self.id_empresa)
        
    class Meta:
        db_table = 'CentroCostos'
        ordering = ["id"]
        verbose_name_plural = "Centro Costos"
        verbose_name = 'Centro Costos'
        managed=True
