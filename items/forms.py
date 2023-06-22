from django import forms
from .models import *


class ItemForm(forms.ModelForm):

    class Meta:
            model = Item
            fields = ['category', 'brand', 'model', 'title', 'description', 'detail', 'quantity', 'condition', 'images', 'price']
            widgets = {
                'title': forms.TextInput(attrs={'size':100}),
                'description': forms.Textarea(attrs={'cols':100}),
                'detail': forms.Textarea(attrs={'cols':100}),
                'images': forms.ClearableFileInput(attrs={'multiple': True}),
            }