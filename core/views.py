from django.shortcuts import render
<<<<<<< HEAD
from django.contrib import messages
from django.http import HttpResponseNotAllowed
from items.models import *
from datetime import datetime
from .forms import ContactoForm


def index(request):
    # filtra los items "NO_VENDIDOS", ordena por fecha de creación donde ultimo >>> primero, mostrando solo 5 items (productos)
    items = Item.objects.filter(sold=False).order_by("-created_at")[:5]


    return render(request, 'core/index.html', {
        'items': items,
    }
    )


def contact(request):
    if request.method == "POST":
        contact_form = ContactoForm(request.POST)
        mensaje = "Recibimos tu consulta. Gracias por escribirnos."
        if contact_form.is_valid():
            messages.success(request, mensaje)
            contact_form = ContactoForm()
        else:
            messages.error(
                request, 'Los datos cargados tienen errores, revísalos')
    elif request.method == "GET":
        contact_form = ContactoForm()
    else:
        HttpResponseNotAllowed(f"Método {request.method} no soportado.")

    context = {
        "contact_form": contact_form
    }

    return render(request, 'core/contact.html', context)
=======
from items.models import *
# Create your views here.

def index(request):
    
    items = Item.objects.filter(is_sold=False) # solo si no estan vendidos
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items' : items,
    })

def contact(request):
    return render(request, 'core/contact.html')
>>>>>>> main
