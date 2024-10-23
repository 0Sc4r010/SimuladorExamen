from django.contrib import admin
from .models import Opciones, Preguntas

# Register your models here.

admin.site.register(Preguntas)
admin.site.register(Opciones)