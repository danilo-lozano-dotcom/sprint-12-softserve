from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Pet
from .forms import PetForm

def pet_list(request):
    pets = Pet.objects.all().order_by('id')
    paginator = Paginator(pets, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pets/pet_list.html', {'page_obj': page_obj})

def pet_register(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mascota registrada exitosamente.")
            return redirect('pet_list')
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
    else:
        form = PetForm()
    return render(request, 'pets/pet_register.html', {'form': form})