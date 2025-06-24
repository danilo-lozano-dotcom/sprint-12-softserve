from django.db import models
from pets.models import Pet

class Appointment(models.Model):
    SERVICE_CHOICES = [
        ('consulta', 'Consulta general y de especialidad'),
        ('vacunacion', 'Vacunación y desparasitación'),
        ('cirugia', 'Cirugías'),
        ('nutricion', 'Control de peso y nutrición'),
        ('urgencia', 'Atención de urgencias'),
        ('laboratorio', 'Laboratorio clínico'),
        ('peluqueria', 'Baño y peluquería'),
    ]
    service = models.CharField(max_length=30, choices=SERVICE_CHOICES, default='consulta')
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE) # Relación con el modelo Pet. Se eliminarán las citas si se elimina la mascota
    date = models.DateTimeField()
    reason = models.TextField()

    def __str__(self):
        return f'Appointment for {self.pet.name} on {self.date}'