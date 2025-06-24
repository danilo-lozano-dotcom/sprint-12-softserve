from django import forms
from .models import Owner

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['name', 'phone', 'email']
        labels = {
            'name': 'Nombre',
            'phone': 'Teléfono',
            'email': 'Correo electrónico',
        }
        
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone.isdigit():
            raise forms.ValidationError("El teléfono solo debe contener números.")
        if len(phone) < 8:
            raise forms.ValidationError("El teléfono debe tener al menos 8 dígitos.")
        return phone