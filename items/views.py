from django.shortcuts import render, get_object_or_404
<<<<<<< HEAD
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import *
from .forms import *

import os
from django.conf import settings
from time import strftime


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)

    # Artículos relacionados
    related_items = Item.objects.filter(category=item.category, sold=False).exclude(id=item.id)[0:1]

    return render(request, 'items/detail.html', {
        'item': item,
        'related_items': related_items,
    }
    )


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemCreateForm
    template_name = 'items/publicar.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('items:detail', kwargs={'pk': self.object.pk})
    
=======
from .models import Item

# Create your views here.

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    # Si un item pertenece a la misma categoria y no está vendido lo muestra en el template
    # related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:5]


    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items,
        }
    )
>>>>>>> main
