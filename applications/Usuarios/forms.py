from django import forms

from .models import Usuarios
class UserForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'})
    )
    
    password2 = forms.CharField(
        label='Repetir Contraseña',
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Repetir Contraseña'})
    )
    
    class Meta:
        model = Usuarios
        fields = ['Correo', 'identificacion', 'Nombre', 'telefono', 'genero', 'Rol', 'Areas_evaluar']
        widgets = {
            'Nombre': forms.TextInput(attrs={'placeholder': 'Apellidos Nombres'}),
            'Correo': forms.EmailInput(attrs={'placeholder': 'correo Valido Micorreo@midomino.com'}),
            'identificacion': forms.TextInput(attrs={'placeholder': 'Documento de identidad'}),
            'telefono': forms.TextInput(attrs={'placeholder': '(000)-999-99-99'}),
            'areas_evaluar': forms.SelectMultiple(attrs={'size': '5'}),  # Asegúrate de que se muestre correctamente
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        
        return cleaned_data

    def clean_identificacion(self):
        documento = self.cleaned_data.get('identificacion')
        if len(documento) < 8:
            raise forms.ValidationError('El documento de identidad debe tener al menos 8 caracteres.')
        return documento

    def clean_ppassword2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2','Las contraseñas no son iguales')
            
    
class LoginForm(forms.Form):  
    Correo = forms.EmailField(  
        label='CorreoUsuario',
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Correo válido: micorreo@midominio.com'})
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'})
    )
