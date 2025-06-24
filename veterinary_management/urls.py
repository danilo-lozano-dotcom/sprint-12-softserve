from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pets/', include('pets.urls')),
    path('owners/', include('owners.urls')),
    path('appointments/', include('appointments.urls')),
    path('services/', views.services, name='services'),
    path('', views.home, name='home'),
]