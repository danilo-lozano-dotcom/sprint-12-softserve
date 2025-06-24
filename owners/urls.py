from django.urls import path
from . import views

urlpatterns = [
    path('', views.owner_list, name='owner_list'),
    path('add/', views.owner_create, name='owner_create'),
]