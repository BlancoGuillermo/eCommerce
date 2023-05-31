from typing import Any, Optional
from django.contrib.admin import register
from django.db import models
from django.db.models.fields import related
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from .models import *
from .forms import *


# def detail(request, pk):
#     item = get_object_or_404(Item, pk=pk)

#     # Artículos relacionados
#     related_items = Item.objects.filter(category=item.category, sold=False).exclude(id=item.id)[0:1]

#     return render(request, 'items/detail.html', {
#         'item': item,
#         'related_items': related_items,
#     }
#     )


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'items/publicar.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.save()

        images = self.request.FILES.getlist('images')

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('items:detail', kwargs={'pk': self.object.pk})

class DetailView(DetailView):
    model = Item
    template_name = 'items/detail.html'
    context_object_name = "item"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = Item.objects.get(pk=self.kwargs["pk"])
        context["related_items"] = Item.objects.filter(category=item.category, sold=False).exclude(pk=item.pk)[:5]

        return context
    
