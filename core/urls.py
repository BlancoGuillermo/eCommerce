from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import *
from .forms import LoginForm


app_name = 'core'

urlpatterns = [
    path('', views.IndexLV.as_view(), name='index'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
