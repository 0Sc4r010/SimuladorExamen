from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from applications.Examenes.models import Categorias
from .manager import UsuariosManager

# Create your models here.
class Usuarios(AbstractBaseUser, PermissionsMixin):
    roles = (
        ('A','Administrador'),
        ('O','Orientador'),
        ('D','Docente'),
        ('E','Estudinte'),
    )
    genero = (
        ('M','Hombre'),
        ('F','Mujer'),
    )
    
    Nombre          = models.CharField('Apellidos y nombres', max_length=100)
    Correo          = models.EmailField(max_length=254, unique=True)
    identificacion  = models.CharField('Documento de identidad',max_length=20, unique=True )
    telefono        = models.CharField('Telefono',max_length=15, blank = True )
    genero          = models.CharField('Genero',max_length=1, choices=genero, blank = True )
    Rol             = models.CharField('Roles', max_length=1, choices=roles, blank = True ) 
    Fecha_Registro  = models.DateTimeField(auto_now=True )
    Areas_evaluar   = models.ManyToManyField(Categorias)
    
    # Campo de contraseña. Este campo es manejado automáticamente por AbstractBaseUser.
   

    # Campos de estado del usuario
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects =  UsuariosManager()  # Asignar el manager personalizado
    
    USERNAME_FIELD = 'Correo'
    REQUIRED_FIELDS = ['identificacion', 'Nombre']
  
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ['Nombre']
    
    def __str__(self):
        return self.Nombre
   