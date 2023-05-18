<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *

=======
from django.shortcuts import render, get_object_or_404
from .models import Item
>>>>>>> 99f5923d28f2cdc0f465e8ecc331ae47c384e21a

# Create your views here.

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    # Si un item pertenece a la misma categoria y no está vendido lo muestra en el template
    # related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:5]


<<<<<<< HEAD
    return render(request, 'items/detail.html', {
=======
    return render(request, 'item/detail.html', {
>>>>>>> 99f5923d28f2cdc0f465e8ecc331ae47c384e21a
        'item': item,
        'related_items': related_items,
        }
    )
<<<<<<< HEAD


def publicar(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            images = request.FILES.getlist('images')
            for image in images:
                item_image = Image.objects.create(image=image)
                item.images.add(item_image)
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm()
    return render(request, 'items/publicar.html', {'item_form': form})
=======
>>>>>>> 99f5923d28f2cdc0f465e8ecc331ae47c384e21a
