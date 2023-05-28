from django import forms
from .models import *


class ItemForm(forms.ModelForm):
    class Meta:
            model = Item
            fields = ['category', 'brand', 'model', 'title', 'description', 'condition', 'price', 'images']
            widgets = {
                'title': forms.TextInput(attrs={'size':80}),
                'description': forms.Textarea(attrs={'cols':80}),
                'images': forms.ClearableFileInput(attrs={'multiple': True}),
            }