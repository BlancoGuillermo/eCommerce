from django.urls import path
from .views import *

app_name = 'items'

urlpatterns = [
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('publicar/', ItemCreateView.as_view(), name='publicar'),
    path('publicaciones/', ItemList.as_view(), name='mis_publicaciones'),
    path('<int:pk>/editar', ItemUpdate.as_view(), name='editar'),
    # path('<int:pk>/eliminar', ItemDelete.as_view(), name='eliminar'),
]