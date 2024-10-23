
from django.contrib import messages  # Corregir la importación de mensajes
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import PreguntaForm, OpcionFormSet
from .models import Preguntas, Opciones
from django.views.generic.list import ListView
from django.views.generic import DeleteView
from django_quill.quill import QuillParseError
from django.utils.html import strip_tags

    
class ListCrudPreguntas(ListView):
    template_name = 'Preguntas/CrudPreguntas.html'
    context_object_name = 'preguntas'  # Cambié a minúsculas para seguir convenciones
    ordering = 'ID_Examen'                                                                                                                                                                                                                                                                                                                                                
    model = Preguntas
    paginate_by = 5
    
    # Renderiza cada una de las plantillas hijas, para pasar una variable de contexto adicional que identifique el tipo de entidad
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entidad'] = 'Preguntas'
        
        # Limpiar el texto de cada pregunta
        preguntas_limpias = []
        for pregunta in context['preguntas']:
            texto_limpio = self.limpiar_texto(pregunta.Texto_Pregunta)
            pregunta.Texto_Pregunta = texto_limpio  # Asigna el texto limpio
            preguntas_limpias.append(pregunta)
        
        context['Preguntas'] = preguntas_limpias  # Actualiza el contexto con las preguntas limpias
        return context
    
    def limpiar_texto(self, texto):
        # Elimina todas las etiquetas HTML y devuelve solo el texto plano
        return strip_tags(texto)  # Esto elimina todas las etiquetas HTML

# El código de la función crear_pregunta_y_opciones permite la creación de una pregunta junto con varias opciones de respuesta,
# utilizando un formulario (para la pregunta) y un conjunto de formularios (para las opciones). 

def crear_pregunta_y_opciones(request):
    if request.method == 'POST':
        pregunta_form = PreguntaForm(request.POST)  # Formulario para la pregunta
        # Se está creando un formset basado en el formulario de opciones, que en este caso se llama OpcionFormSet.
        # Un formset es un conjunto de formularios que permite gestionar múltiples instancias del mismo formulario 
        # (en este caso, múltiples opciones asociadas a una pregunta).
        formset = OpcionFormSet(request.POST, queryset=Opciones.objects.none())  # Formset para las opciones

        try:
            if pregunta_form.is_valid() and formset.is_valid():
                # Guardar la pregunta
                nueva_pregunta = pregunta_form.save()  # Crea y guarda la nueva pregunta

                # Guardar las opciones asociadas a la pregunta
                for opcion_form in formset:
                    if opcion_form.cleaned_data:  # Verifica que el formulario de opción tenga datos válidos
                        nueva_opcion = opcion_form.save(commit=False)
                        nueva_opcion.ID_Pregunta = nueva_pregunta  # Asignar la pregunta a la opción
                        nueva_opcion.save()

                # Mensaje de éxito
                messages.success(request, "Pregunta y opciones guardadas exitosamente.")

                # Redirigir a la misma vista o a otra vista según sea necesario
                return render(request, 'Preguntas/CreaPreguntas.html', {
                    'pregunta_form': PreguntaForm(),  # Reiniciar el formulario
                    'formset': OpcionFormSet(queryset=Opciones.objects.none()),  # Reiniciar el formset
                })
        except QuillParseError as e:
            print(f"Error al procesar Quill: {str(e)}")
            messages.error(request, "Error al procesar el contenido de la pregunta.")  # Mensaje de error
        except Exception as e:
            print(f"Error inesperado: {str(e)}")
            messages.error(request, "Ocurrió un error inesperado al guardar los datos.")  # Mensaje de error

    else:
        pregunta_form = PreguntaForm()  # Formulario vacío para la pregunta
        formset = OpcionFormSet(queryset=Opciones.objects.none())  # Formset vacío para las opciones

    return render(request, 'Preguntas/CreaPreguntas.html', {'pregunta_form': pregunta_form, 'formset': formset})


class PreguntaDeleteView(DeleteView):
    model = Preguntas
    template_name = "Preguntas/DeletePreg.html"
    success_url =  reverse_lazy('Preguntas:crudPreg')
    