from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from .models import *
from .forms import *


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'items/create_item.html'
    login_url = 'login'
    

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('items:detail', kwargs={'pk': self.object.pk})


class DetailView(DetailView):
    model = Item
    template_name = 'items/detail_item.html'
    context_object_name = "item"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = Item.objects.get(pk=self.kwargs["pk"])
        context["related_items"] = Item.objects.filter(category=item.category, sold=False).exclude(pk=item.pk)[:5] | Item.objects.filter(category=item.category.parent, sold=False).exclude(pk=item.pk)[:5]

        return context

class ItemList(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'items/list_item.html'
    context_object_name = 'item_list'
    login_url = 'login'

    def get_queryset(self):
        user = self.request.user
        return Item.objects.filter(sold=False, created_by=user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ItemUpdate(UpdateView):
    model = Item
    fields = ['category', 'brand', 'model', 'title', 'description', 'detail', 'quantity', 'condition', 'images', 'price']
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('items:mis_publicaciones')
