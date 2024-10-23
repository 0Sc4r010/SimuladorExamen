from django.db import models
from django.contrib.auth.models import BaseUserManager


class UsuariosManager(BaseUserManager, models.Manager):
    
    def _create_user(self, Correo, identificacion, password, is_staff, is_superuser, **extra_fields):
        """
        Método base para la creación de usuarios. Se utiliza tanto para usuarios normales
        como para superusuarios.
        """
        extra_fields.setdefault('is_active', True)  # Asegura que el usuario esté activo por defecto
        user = self.model(
            Correo=Correo,
            identificacion=identificacion,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)  # Encripta la contraseña
        user.save(using=self._db)  # Guarda el usuario en la base de datos
        return user

    def create_user(self, Correo, identificacion, password, **extra_fields):
        """
        Crea un usuario normal con `is_staff=False` y `is_superuser=False`.
        """
        return self._create_user(Correo, identificacion, password, False, False, **extra_fields)

    def create_superuser(self, Correo, identificacion, password=None, **extra_fields):
        """
        Crea un superusuario con `is_staff=True` y `is_superuser=True`.
        """
        return self._create_user(Correo, identificacion, password, True, True, **extra_fields)

    def buscar_por_identificacion(self, identificacion):
        """
        Retorna el usuario que coincide con la identificación proporcionada.
        Si no se encuentra, retorna None.
        """
        try:
            return self.get(identificacion=identificacion)
        except self.model.DoesNotExist:
            return None
        
    def buscar_por_correo(self, correo):
        """
        Retorna la identificación del usuario que coincide con el correo proporcionado.
        Si no se encuentra, retorna None.
        """
        try:
            usuario = self.get(Correo=correo)
            return usuario.identificacion  # Retorna la identificación del usuario
        except self.model.DoesNotExist:
            return None    
        

    def buscar_por_nombre(self, nombre):
        """
        Retorna una lista de usuarios cuyo nombre contiene la cadena proporcionada (búsqueda case-insensitive).
        """
        return self.filter(nombre__icontains=nombre)

    def todos_los_usuarios(self):
        """
        Retorna todos los usuarios en el sistema.
        """
        return self.all()

