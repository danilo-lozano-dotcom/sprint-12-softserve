from django.shortcuts import render

def home(request):
    return render(request, 'home.html') # Renderiza la página de inicio usando la plantilla home.html

def services(request):
    return render(request, 'services.html')