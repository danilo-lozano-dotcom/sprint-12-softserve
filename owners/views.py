from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Owner
from .forms import OwnerForm

def owner_list(request):
    owners = Owner.objects.all().order_by('id')
    paginator = Paginator(owners, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'owners/owner_list.html', {'page_obj': page_obj})

def owner_create(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Propietario registrado exitosamente.")
            return redirect('owner_list')
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
    else:
        form = OwnerForm()
    return render(request, 'owners/owner_form.html', {'form': form})