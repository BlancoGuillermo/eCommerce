from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('publicar/', views.publicar, name='publicar'),

]