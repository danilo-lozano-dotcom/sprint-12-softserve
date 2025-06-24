from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Appointment
from .forms import AppointmentForm

def appointment_list(request):
    appointments = Appointment.objects.all().order_by('id') # Ordena para paginación consistente
    paginator = Paginator(appointments, 10) # 10 consultas por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'appointments/appointment_list.html', {'page_obj': page_obj})

def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Consulta registrada exitosamente.")
            return redirect('appointment_list')
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
    else:
        form = AppointmentForm()
    return render(request, 'appointments/appointment_form.html', {'form': form}) # Renderiza el formulario