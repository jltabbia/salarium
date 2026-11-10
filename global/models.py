from django.db import models

# Create your models here.
class Provincias(models.Model):
    codigo=models.IntegerField('Código',null=True, blank=True)
    nombre=models.CharField('Nombre de la Provincia',max_length=50,null=True, blank=True)
        
    def __str__(self):
        return '%s,%s,%s' % (self.id, self.codigo, self.nombre)
        
    class Meta:
        db_table = 'provincias'
        ordering = ["codigo"]
        verbose_name_plural = "Provincias"
        verbose_name = 'Provincias'
        managed=True

class Localidades(models.Model):
    codigo=models.IntegerField('Código',null=True, blank=True)
    id_provincia=models.ForeignKey('Provincias',on_delete=models.CASCADE)
    nombre=models.CharField('Nombre de la Categoria',max_length=100,null=True, blank=True)
        
    def __str__(self):
        return '%s,%s,%s, %s' % (self.id, self.id_provincia, self.codigo, self.nombre)
        
    class Meta:
        db_table = 'localidades'
        ordering = ["id_provincia","codigo"]
        verbose_name_plural = "Localidades"
        verbose_name = 'Localidades'
        managed=True

class Empresas(models.Model):

    nombre=models.CharField('Nombre de la Empresa',max_length=100,null=True, blank=True)
    domicilio=models.CharField('Domicilio',max_length=100,null=True, blank=True)
    id_provincia=models.ForeignKey('Provincias',on_delete=models.CASCADE)
    id_localidad=models.ForeignKey('Localidades',on_delete=models.CASCADE)

    def __str__(self):
        return '%s,%s,%s,%s,%s' % (self.id, self.nombre, self.domicilio, self.id_provincia, self.id_localidad)
        
    class Meta:
        db_table = 'empresas'
        ordering = ["nombre"]
        verbose_name_plural = "Empresas"
        verbose_name = 'Empresas'
        managed=True