from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Item
        fields = ['category', 'name', 'description', 'price', 'images']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 40, 'rows': 10}),
        }