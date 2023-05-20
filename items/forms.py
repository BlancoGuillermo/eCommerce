from django import forms
from .models import Item

class ItemCreateForm(forms.ModelForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Item
        fields = ['category', 'title', 'brand', 'model', 'description', 'price', 'images']