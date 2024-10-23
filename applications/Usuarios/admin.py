from django.contrib import admin
from .models import Usuarios

# Register your models here.

class UsuariosAdmin(admin.ModelAdmin):
    list_display = (
            'Nombre',        
            'Correo',        
            'identificacion',
            'telefono',      
            'genero',       
            'Rol',           
            'Fecha_Registro',
        )
    
    search_fields = ('Nombre',)
    
admin.site.register(Usuarios,UsuariosAdmin)    
