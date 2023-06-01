from django.urls import path
from .views import *

app_name = 'items'

urlpatterns = [
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('publicar/', ItemCreateView.as_view(), name="publicar"),
]