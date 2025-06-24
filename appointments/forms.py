from django import forms
from .models import Appointment
from django.utils import timezone

class AppointmentForm(forms.ModelForm):
    service = forms.ChoiceField(
        choices=[('', 'Selecciona una opción')] + Appointment.SERVICE_CHOICES,
        label='Servicio'
    )
    
    class Meta:
        model = Appointment
        fields = ['date', 'service', 'reason', 'pet']
        labels = {
            'date': 'Fecha y hora',
            'service': 'Servicio',
            'reason': 'Motivo',
            'pet': 'Mascota',
        }
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
     
    # Función para validar fechas actuales y evitar que se agenden citas en el pasado    
    def clean_date(self):
        date = self.cleaned_data['date']
        if date < timezone.now():
            raise forms.ValidationError("No puedes agendar una consulta en el pasado.")
        return date