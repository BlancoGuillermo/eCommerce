from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
import os
from datetime import datetime


# Create your views here.

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    # Si un item pertenece a la misma categoria y no está vendido lo muestra en el template
    # related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:5]


    return render(request, 'items/detail.html', {
        'item': item,
        'related_items': related_items,
        }
    )


def publicar(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            images = request.FILES.getlist('images')
            for image in images:
                # Obtener la extensión del archivo
                _, ext = os.path.splitext(image.name)
                # Generar el nuevo nombre de la imagen
                new_name = f"{item.pk}_{datetime.now().strftime('%Y%m%d%H%M%S')}{ext}"
                # Guardar la imagen en el directorio correspondiente
                item_image = Image.objects.create(image=image)
                item_image.image.save(new_name, image, save=True)
                item.images.add(item_image)
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm()
    return render(request, 'items/publicar.html', {'item_form': form})