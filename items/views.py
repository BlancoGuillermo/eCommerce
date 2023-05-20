from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import *
from .forms import *


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)

    # Artículos relacionados
    related_items = Item.objects.filter(
        category=item.category, sold=False).exclude(pk=pk)[0:5]

    return render(request, 'items/detail.html', {
        'item': item,
        'related_items': related_items,
    }
    )


class ItemCreateView(CreateView):
    form_class = ItemCreateForm
    template_name = 'items/publicar.html'
    success_url = reverse_lazy('items:detail')  # URL a la que redireccionar después de la creación exitosa

    def form_valid(self, form):
        form.instance.created_by = self.request.user  # Establece el usuario creador como el usuario actual
        return super().form_valid(form)

