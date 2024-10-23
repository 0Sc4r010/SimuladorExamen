from django.urls import path
from . import views
from .views import crear_pregunta_y_opciones  # Asegúrate de que esta importación sea correcta

app_name = 'Preguntas'

urlpatterns = [
    path('crear_pregunta_y_opciones/', crear_pregunta_y_opciones, name='crear_pregunta'),
    path('liscrudPreguntas/', views.ListCrudPreguntas.as_view(), name = 'crudPreg'),
    path('DeletePreg/<pk>/', views.PreguntaDeleteView.as_view(), name = 'Delprg'),
]
