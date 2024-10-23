from django.db import models


class ExamenManager(models.Manager):
 
    def evalua_usr(self, usuario):
        
        examenes = self.filter(Categoria__in=usuario.Areas_evaluar.all())
        return self.filter(id__in=examenes)
