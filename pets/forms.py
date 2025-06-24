from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'age', 'owner']
        labels = {
            'name': 'Nombre',
            'species': 'Especie',
            'age': 'Edad',
            'owner': 'Propietario',
        }
        
    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 0:
            raise forms.ValidationError("La edad no puede ser negativa.")
        return age