from django.db import models
from applications.Examenes.models import Examenes
from django_quill.fields import QuillField

from .manager import PreguntaManager

# Create your models here.




class Preguntas(models.Model):
    
    Niveles_examen = (
        ('B', 'Basico'),
        ('M', 'Intermedio'),
        ('A', 'Avanzado'),
    )
    
    Texto_Pregunta = models.TextField('Descripción')  # QuillField() 
    ID_Examen = models.ForeignKey(Examenes,on_delete=models.CASCADE)
    Nivel_Dificultad = models.CharField('Niveles', max_length=1, choices=Niveles_examen)
    objects = PreguntaManager()
         
    class Meta:
        verbose_name = "Preguntas del Examen"
        verbose_name_plural = "Preguntas"
         
     
    def __str__(self):
        return f"{self.Texto_Pregunta}+ '-' + {self.Nivel_Dificultad}"



class Opciones(models.Model):
    OPCIONES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    ]
    
    Codigo_Opcion = models.CharField('id Opciones',max_length=1,choices=OPCIONES)
    Texto_Opción = models.CharField('opcion', max_length=200,blank=False)
    Es_Correcta = models.BooleanField(default=False)
    ID_Pregunta = models.ForeignKey(Preguntas,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Opciones del Examen"
        verbose_name_plural = "Opciones"
        
    def save(self, *args, **kwargs):
        if not self.Codigo_Opcion:  # Asignar automáticamente solo si no hay código asignado
            opciones_existentes = Opciones.objects.filter(ID_Pregunta=self.ID_Pregunta).count()
            self.Codigo_Opcion = chr(65 + opciones_existentes)  # A, B, C, D, etc.
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Texto_Opción