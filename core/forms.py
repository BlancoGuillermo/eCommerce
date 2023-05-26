import re
from django import forms
from django.forms import ValidationError


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