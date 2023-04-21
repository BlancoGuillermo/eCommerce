from django.shortcuts import render, get_object_or_404
from .models import Item

# Create your views here.

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    # Si un item pertenece a la misma categoria y no está vendido lo muestra en el template
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:5]


    return render(request, 'items/detail.html', {
        'item': item,
        'related_items': related_items,
        }
    )
