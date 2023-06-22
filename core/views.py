from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib import messages
from items.models import *
from .forms import *
from django.views.generic import ListView, FormView


class IndexLV(ListView):
    model = Item
    template_name = 'core/index.html'
    extra_context = {'form': SearchForm()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            item_list = Item.objects.filter(Q(sold=False) &
                                            Q(title__icontains=query)|
                                            Q(brand__icontains=query)|
                                            Q(model__icontains=query))
        else:
            item_list = Item.objects.filter(Q(sold=False)).order_by("-created_at")

        return item_list


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'core/contact.html'
    success_url = reverse_lazy('core:index')
    "¡Consulta enviada correctamente!\nNos comunicaremos a la brevedad"

    def form_valid(self, form):
        messages.success(self.request, "¡Consulta enviada correctamente!\nNos comunicaremos a la brevedad")
        
        return super().form_valid(form)