# forms.py
from django import forms
from .models import Preguntas, Opciones
from django_quill.forms import QuillFormField
from django.forms import modelformset_factory

class PreguntaForm(forms.ModelForm):
    Texto_Pregunta = QuillFormField()
    class Meta:
        model = Preguntas
        fields = ['Texto_Pregunta', 'Nivel_Dificultad', 'ID_Examen']  # Agregar examen como un campo

class OpcionForm(forms.ModelForm):
    class Meta:
        model = Opciones
        fields = ['Texto_Opción', 'Es_Correcta']  # Eliminamos 'pregunta' para manejarlo en la vista

# Crear un formset para las opciones
OpcionFormSet = modelformset_factory(Opciones, form=OpcionForm, extra=4)  # Puedes cambiar 'extra' según sea necesario

class PreguntaOpcionForm(forms.Form):
    pregunta = PreguntaForm()
    opciones = OpcionForm()  # Puedes usar un formulario con múltiples opciones si es necesario
    
