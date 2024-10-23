from django.db import models
from applications.Usuarios.models import Usuarios
from applications.Preguntas.models import Preguntas 

# Create your models here.

class Respuestas(models.Model):
    ID_Usuario = models.ForeignKey(Usuarios,on_delete = models.CASCADE) 
    ID_Pregunta = models.ForeignKey(Preguntas,on_delete = models.CASCADE) 
    Código_Opción = models.CharField('respuesta',max_length=1,blank=False)
    Fecha_Respuesta = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = "Respuestas del Usuario"
        verbose_name_plural = "Respuestas"
    
    def __str__(self):
        return self.nombre
        
