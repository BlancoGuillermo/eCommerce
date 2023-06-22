import re
from django import forms
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
    }))



class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'nombre de usuario',
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'pepito@correo.com',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'ingresá tu password',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
    }))

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user



def solo_letras(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('El nombre solo admite letras. %(valor)s',
                            code='Invalid',
                            params={'valor': value})


def custom_validate_email(value):
    email_regex = r'^([\w\-\.]+)@((\[([0-9]{1,3}\.){3}[0-9]{1,3}\])|(([\w\-]+\.)+)([a-zA-Z]{2,4}))$'
    if not re.match(email_regex, value):
        raise ValidationError('Correo electrónico inválido')


class ContactForm(forms.Form):
    nombre = forms.CharField(
        label='Nombre',
        max_length=50,
        validators=(solo_letras,),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Solo letras'
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        max_length=100,
        required=False,
        validators=(custom_validate_email,),
        error_messages={
            'required': 'Por favor completa el campo'
        },
        widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'})
    )
    asunto = forms.CharField(
        label='Asunto',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    mensaje = forms.CharField(
        label='Mensaje',
        max_length=500,
        widget=forms.Textarea(attrs={
            'rows': 5, 
            'class': 'form-control',
            'placeholder': '20 caracteres mínimo',
            }
        )
    )

    def clean_mensaje(self):
        data = self.cleaned_data['mensaje']
        if len(data) < 20:
            raise ValidationError(
                "El mensaje es un acotado, proporciona más detalles.")
        return data

    def clean(self):
        cleaned_data = super().clean()
        asunto = cleaned_data.get("asunto")


class SearchForm(forms.Form):
    q = forms.CharField(
        label='Busqueda',
        required=False,
        min_length=3,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre del producto o palabras claves'
            }
        )
    )