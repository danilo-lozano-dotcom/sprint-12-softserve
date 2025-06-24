from django.urls import path
from . import views

urlpatterns = [
    path('', views.pet_list, name='pet_list'),
    path('registrar/', views.pet_register, name='pet_register'),
]