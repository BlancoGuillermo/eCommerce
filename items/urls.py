from django.urls import path
from . import views
from .views import *

app_name = 'items'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('publicar/', ItemCreateView.as_view(), name="publicar"),

    # # deberia renderizar una lista de los items creados por el usuario para que edite o elimine
    # path('editar/', ItemUpdateView.as_view(), name="item_update"),
]