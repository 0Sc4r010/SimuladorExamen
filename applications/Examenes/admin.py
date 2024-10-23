from django.contrib import admin
from .models import Examenes,Categorias 

# Register your models here.

admin.site.register(Categorias)

class ExamenAdmin(admin.ModelAdmin):
    list_display = (
        'Nombre_Examen',  
        'Descripcion',    
        'Fecha_Creacion', 
        'Duracion_Limite',
        'Categoria',
        )
    
    search_fields = ('Nombre_Examen',)
    
admin.site.register(Examenes,ExamenAdmin)    