from django.shortcuts import render
from items.models import *
from datetime import datetime

def index(request):
    # filtra los items "NO_VENDIDOS", ordena por fecha de creación donde ultimo >>> primero, mostrando solo 4 elementos
    items = Item.objects.filter(is_sold=False).order_by("-created_at")[:4]

    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items' : items,
    })

def contact(request):
    return render(request, 'core/contact.html')
