# Create your views here.

from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator





from applications.Preguntas.models import Opciones, Preguntas
from applications.Respuestas.models import Respuestas
from applications.Usuarios.models import Usuarios
from .models import Examenes
from .forms import ExaForm


# Esta vista lista todos los exámenes y permite filtrar por el nombre del examen usando un campo de búsqueda.
# Los resultados están paginados a 10 exámenes por página

class ListAllExamenes(ListView):
    template_name = 'Examenes/listaExamanes.html'
    context_object_name = 'Examenes'
    paginate_by = 10
    def get_queryset(self) :
        palabra_clave = self.request.GET.get("kword",'')
        lista = Examenes.objects.filter(
           Nombre_Examen__icontains =  palabra_clave 
        )
        return lista
    
    
# Muestra una lista de exámenes en una vista CRUD (Crear, Leer, Actualizar, Eliminar), con paginación.

class ListCrudExamenes(ListView):
    template_name = 'Examenes/CrudExamenes.html'
    context_object_name = 'Examenes'
    ordering = 'Nombre_Examen'                                                                                                                                                                                                                                                                                                                                                
    model = Examenes
    paginate_by = 5
    # renderiza cada una de las plantillas hijas, para pasar una variable de contexto adicional que identifique el tipo de entidad
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entidad'] = 'examenes'
        return context
    
    
# Esta vista gestiona la creación de nuevos exámenes.   
    
class CreateExamenes(CreateView):
    model = Examenes
    template_name = 'Examenes/CreateExamenes.html'
    form_class = ExaForm
    success_url =  reverse_lazy('Examenes:Crudcexa')
    
# Proporciona una vista detallada de un examen específico.

class ExamenesDetailView(DetailView):
    model = Examenes
    template_name = "Examenes/DetalleExamenes.html"
    
# Gestiona la eliminación de un examen.      
class ExamenesDeleteView(DeleteView):
    model = Examenes
    template_name = "Examenes/DeletExamenes.html"
    success_url =  reverse_lazy('Examenes:Crudcexa')
    
  
# Esta vista gestiona la actualización de los datos de un examen.
class ExamenesUpdateView(UpdateView):
    model = Examenes
    template_name = "Examenes/UpdateExamenes.html"
    form_class = ExaForm
    success_url =  reverse_lazy('Examenes:Crudcexa')

    def form_valid(self, form):
        print("Datos del formulario:", form.cleaned_data)  # Muestra los datos del formulario
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("Errores de validación:", form.errors)  # Muestra los errores de validación
        return super().form_invalid(form)
    
# Esta función genera las preguntas asociadas a los exámenes que un usuario debe realizar.

def preguntas_x_usuario(request):
   
    usuario = Usuarios.objects.buscar_por_identificacion('79485589')
    examenes =  Examenes.objects.evalua_usr(usuario) 
    preguntas = Preguntas.objects.filter(ID_Examen__in=examenes)  # Filtra las preguntas relacionadas con los exámenes
     
    preguntas_con_opciones = []
    
    preguntas_con_opciones = []
    for pregunta in preguntas:
        opciones = Opciones.objects.filter(ID_Pregunta=pregunta)
        preguntas_con_opciones.append({
            'pregunta': pregunta,
            'opciones': opciones
        })
    
    return render(request, 'Examenes/Evaluar.html', {'examenes': examenes, 'preguntas_con_opciones': preguntas_con_opciones})

# Esta vista permite evaluar al usuario mostrando los exámenes y preguntas correspondientes.
@method_decorator(login_required, name='dispatch')
class EvaluarUsuarioView(View):
   
    def get(self, request):
        identificacion = request.session.get('identificacion')
        usuario = Usuarios.objects.buscar_por_identificacion(identificacion)  
        examenes = Examenes.objects.evalua_usr(usuario)
        
        # Calcular la duración total de todos los exámenes
        total_duracion = sum(examen.Duracion_Limite for examen in examenes)

        # Depuración: Imprimir exámenes y su duración
        print(f"Exámenes: {examenes}")  # Agregar esto para depurar
        print(f"Duración total: {total_duracion} minutos")  # Agregar esto para depurar
        
        preguntas = Preguntas.objects.filter(ID_Examen__in=examenes)

        return render(request, 'Examenes/Evaluar.html', {
            'examenes': examenes,
            'preguntas': preguntas,
            'total_duracion': total_duracion 
        })



@method_decorator(login_required, name='dispatch')
class GuardarRespuestasView(View):
    def post(self, request):
        identificacion = request.session.get('identificacion')
        usuario = Usuarios.objects.buscar_por_identificacion(identificacion)  
        for key, value in request.POST.items():
            if key.startswith('respuesta_'):
                pregunta_id = key.split('_')[1]
                codigo_opcion = value

                # Guardar la respuesta en la base de datos
                Respuestas.objects.create(
                    ID_Usuario=usuario,
                    ID_Pregunta_id=pregunta_id,
                    Código_Opción=codigo_opcion
                )
        
        return render(request, 'Examenes/exito.html')  # Muestra la plantilla de éxito

# Muestra los resultados de los exámenes presentados por el usuario.
    
@method_decorator(login_required, name='dispatch')   
class ResultadosView(View):
    def get(self, request):
        identificacion = request.session.get('identificacion')
        # Suponiendo que tienes un usuario identificado de alguna manera
        usuario = Usuarios.objects.buscar_por_identificacion(identificacion)  # Cambia esto según tu lógica

        # Filtramos las respuestas del usuario
        respuestas = Respuestas.objects.filter(ID_Usuario=usuario)

        resultados_examenes = {}
        total_correctas = 0
        total_preguntas = respuestas.count()

        # Recorremos las respuestas del usuario
        for respuesta in respuestas:
            pregunta = Preguntas.objects.get(id=respuesta.ID_Pregunta.id)
            examen = pregunta.ID_Examen  # Obtenemos el examen relacionado con la pregunta
            opcion_correcta = pregunta.opciones_set.filter(Es_Correcta=True).first()  # Opción correcta de la pregunta
            
            if opcion_correcta:
            # Accede a los atributos de opcion_correcta
                print(opcion_correcta.Codigo_Opcion)  # o lo que necesites hacer con esta opción
            else:
                print("No hay opción correcta para esta pregunta.")

            # Si el examen aún no está en el diccionario, lo añadimos
            if examen.Nombre_Examen not in resultados_examenes:
                resultados_examenes[examen.Nombre_Examen] = []

            # Añadimos los detalles de la pregunta y si fue correcta o no
            resultados_examenes[examen.Nombre_Examen].append({
                'pregunta': pregunta.Texto_Pregunta,
                'respuesta_usuario': respuesta.Código_Opción,
                'respuesta_correcta': opcion_correcta.Codigo_Opcion,
                'es_correcta': respuesta.Código_Opción == opcion_correcta.Codigo_Opcion
            })

            # Contamos las correctas
            if respuesta.Código_Opción == opcion_correcta.Codigo_Opcion:
               total_correctas += 1

        puntaje = (total_correctas / total_preguntas) * 100 if total_preguntas > 0 else 0
        
        return render(request, 'Examenes/resultados.html', {
            'resultados_examenes': resultados_examenes,
            'puntaje': puntaje,
            'total_correctas': total_correctas,
            'total_preguntas': total_preguntas,
        })
