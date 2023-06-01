from django.urls import reverse_lazy
from django.contrib import messages
from items.models import *
from .forms import *
from django.views.generic import ListView, FormView


# def contact(request):
#     if request.method == "POST":
#         contact_form = ContactoForm(request.POST)
#         mensaje = "Recibimos tu consulta. Gracias por escribirnos."
#         if contact_form.is_valid():
#             messages.success(request, mensaje)
#             contact_form = ContactoForm()
#         else:
#             messages.error(
#                 request, 'Los datos cargados tienen errores, revísalos')
#     elif request.method == "GET":
#         contact_form = ContactoForm()
#     else:
#         HttpResponseNotAllowed(f"Método {request.method} no soportado.")

#     context = {
#         "contact_form": contact_form
#     }

#     return render(request, 'core/contact.html', context)

class IndexLV(ListView):
    model = Item
    template_name = 'core/index.html'

    def get_queryset(self):
        return Item.objects.filter(sold=False).order_by("-created_at")[:5]


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'core/contact.html'
    success_url = reverse_lazy('core:index')
    "¡Consulta enviada correctamente!\nNos comunicaremos a la brevedad"

    def form_valid(self, form):
        messages.success(self.request, "¡Consulta enviada correctamente!\nNos comunicaremos a la brevedad")
        
        return super().form_valid(form)
