from django.urls import path
from . import views

app_name = 'Examenes'

urlpatterns = [
    path('listaExamanes/', views.ListAllExamenes.as_view(), name = 'Listexa'),
    path('liscrudExamanes/', views.ListCrudExamenes.as_view(), name = 'Crudcexa'),
    path('CreateExamanes/', views.CreateExamenes.as_view(), name = 'CreaExa'),
    path('DetalleExamanes/<pk>/', views.ExamenesDetailView.as_view(), name = 'VerExa'),
    path('UpdateExamanes/<pk>/', views.ExamenesUpdateView.as_view(), name = 'UpdExa'),
    path('DeletExamenes/<pk>/', views.ExamenesDeleteView.as_view(), name = 'DelExa'),
    path('Evaluar/', views.EvaluarUsuarioView.as_view(), name='evaluar_usuario'),
    path('guardar_respuestas/', views.GuardarRespuestasView.as_view(), name='guardar_respuestas'),
    path('resultados/', views.ResultadosView.as_view(), name='resultados'),
]
