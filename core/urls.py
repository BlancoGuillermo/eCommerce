from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('contact/', views.contact, name='contact'),
    path('', views.IndexLV.as_view(), name='index'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
