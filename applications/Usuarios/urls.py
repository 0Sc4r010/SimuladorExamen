from django.urls import path
from . import views

app_name = 'Usuarios'

urlpatterns = [
    path('', views.InicioView.as_view(), name = 'inicio'),
    path('login/', views.LoginUser.as_view(), name = 'login'),
    path('listaUsuarios/', views.ListAllUsuarios.as_view(), name = 'Listau'),
    path('liscrudUsuarios/', views.ListCrudUsuarios.as_view(), name = 'Listcrud'),
    path('CreateUser/', views.CreateUsers.as_view(), name = 'Creausr'),
    path('DetalleUser/<pk>/', views.UsuarioDetailView.as_view(), name = 'Verusr'),
    path('UpdateUser/<pk>/', views.UsuarioUpdateView.as_view(), name = 'Updusr'),
    path('DeleteUser/<pk>/', views.UsuarioDeleteView.as_view(), name = 'Delusr'),

]

