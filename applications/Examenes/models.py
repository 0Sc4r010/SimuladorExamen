from django.db import models
from datetime import date
from django.utils.translation import gettext_lazy as _

from .manager import ExamenManager


class Categorias(models.Model):
    ID_Categoria  = models.CharField('Area tematica',max_length=6,unique=True)
    Nombre_Categoria = models.CharField('nombre Area',max_length=30)
    
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        
    def __str__(self):
        return self.ID_Categoria + '-' + self.Nombre_Categoria



# Create your models here.
class Examenes(models.Model):
    Nombre_Examen   = models.CharField('Area tematica',max_length=30,unique=True)
    Descripcion     = models.TextField('Descripción') 
    Fecha_Creacion  = models.DateField(_("Fecha de creacion"), default=date.today)
    Duracion_Limite = models.IntegerField('Duracion en minutos',default=5, null=False, blank=False)
    Categoria       = models.ForeignKey(Categorias,on_delete=models.CASCADE )
    objects = ExamenManager()  # Asignar el manager personalizado
    
    class Meta:
        verbose_name = "Examen"
        verbose_name_plural = "Examenes"
        
    def __str__(self):
        return self.Nombre_Examen