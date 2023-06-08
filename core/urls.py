from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from views import *
from .forms import LoginForm


app_name = 'core'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('contact/', views.contact, name='contact'),
    path('', views.IndexLV.as_view(), name='index'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),

]
