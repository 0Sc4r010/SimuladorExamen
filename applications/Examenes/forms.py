from django import forms
from .models import Examenes

class ExaForm(forms.ModelForm):

    class Meta:
        model = Examenes
        fields = ('Nombre_Examen', 'Duracion_Limite', 'Descripcion', 'Categoria')  # Excluyendo Fecha_Creación
        widgets = {
            'Nombre_Examen': forms.TextInput(attrs={'placeholder': 'Identificación del Examen', 'style': 'width: 350px;'}),
             'Duracion_Limite': forms.NumberInput(attrs={'placeholder': 'Duración en minutos de la prueba','min': 1,  # Valor mínimo permitido
                'style': 'width: 100%;'  
            }),
            'Descripcion': forms.Textarea(attrs={'placeholder': 'Breve detalle del examen', 'rows': 10, 'cols': 80}),
        }

        # Agregar QuillFormField directamente para la descripción
   