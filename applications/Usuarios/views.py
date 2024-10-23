# Create your views here.



from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView  
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from applications import Respuestas
from .models import Usuarios
from .forms import LoginForm, UserForm
from django.contrib.auth import authenticate, login



class LoginUser(FormView):
    template_name = 'Usuarios/Login.html'
    form_class = LoginForm
    success_url =  reverse_lazy('Usuarios:inicio')
   
    def form_valid(self, form):
        user = authenticate( 
            Correo=form.cleaned_data['Correo'],
            password=form.cleaned_data['password'])
        
        if user is not None:
        # Si el usuario existe y la autenticación es exitosa, iniciamos sesión
            login(self.request, user)
            self.request.session['identificacion'] = user.identificacion
            print(user.identificacion)
            return super(LoginUser, self).form_valid(form)
        else:
        # Si la autenticación falla, mostramos un mensaje de error
            form.add_error(None, "Correo o contraseña incorrectos.")
            return self.form_invalid(form)


class InicioView(TemplateView):
    template_name = 'home/inicio.html'
 
class ListAllUsuarios(ListView):
    template_name = 'Usuarios/listaUsuarios.html'
    context_object_name = 'Usuarios'
    paginate_by = 10
    def get_queryset(self) :
        palabra_clave = self.request.GET.get("kword",'')
        lista = Usuarios.objects.filter(
           identificacion__icontains =  palabra_clave 
        )
        return lista
    
    
class ListCrudUsuarios(ListView):
    template_name = 'Usuarios/CrudUsuarios.html'
    context_object_name = 'Usuarios'
    ordering = 'Nombre'                                                                                                                                                                                                                                                                                                                                                
    model = Usuarios
    paginate_by = 5
    
    # renderiza cada una de las plantillas hijas, para pasar una variable de contexto adicional que identifique el tipo de entidad
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entidad'] = 'usuarios'
        return context
    
    
class CreateUsers(FormView):
    model = Usuarios
    template_name = 'Usuarios/CreateUser.html'
    form_class = UserForm
    success_url =  reverse_lazy('Usuarios:Listcrud')
    
    def form_valid(self, form):
        # Crea el usuario
        user = Usuarios.objects.create_user(
            Correo=form.cleaned_data['Correo'],
            identificacion=form.cleaned_data['identificacion'],
            password=form.cleaned_data['password1'],
            Nombre=form.cleaned_data['Nombre'],
            telefono=form.cleaned_data['telefono'],
            genero=form.cleaned_data['genero'],
            Rol=form.cleaned_data['Rol'],
            
        )
        
        # Asigna las áreas a evaluar al usuario
        areas_a_evaluar = form.cleaned_data['Areas_evaluar']
        user.Areas_evaluar.set(areas_a_evaluar)  
        print("Usuario creado:", user)  # Verificación en consola
        
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("Errores de validación:", form.errors)
        return super().form_invalid(form)


class UsuarioDetailView(DetailView):
    model = Usuarios
    template_name = "Usuarios/DetalleUser.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.get_object()

        # Aquí recuperas las respuestas del usuario
        respuestas_correctas =  10 #  Respuestas.objects.filter(usuario=usuario, es_correcta=True).count()
        respuestas_incorrectas = 5 # Respuestas.objects.filter(usuario=usuario, es_correcta=False).count()

        # Pasar las variables al contexto
        context['correctas'] = respuestas_correctas
        context['incorrectas'] = respuestas_incorrectas

        return context
    
    
    
    
    

class UsuarioUpdateView(UpdateView):
    model = Usuarios
    template_name = "Usuarios/UpdateUser.html"
    form_class = UserForm
    success_url =  reverse_lazy('Usuarios:Listcrud')
    
class UsuarioDeleteView(DeleteView):
    model = Usuarios
    template_name = "Usuarios/DeleteUser.html"
    success_url =  reverse_lazy('Usuarios:Listcrud')
    
