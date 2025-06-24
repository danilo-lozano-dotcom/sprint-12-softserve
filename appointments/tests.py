from django.test import TestCase
from .models import Appointment
from pets.models import Pet
from owners.models import Owner
from django.utils import timezone

class AppointmentModelTest(TestCase):

    def setUp(self):
        self.owner = Owner.objects.create(name="John Doe", phone="1234567890", email="john@example.com")
        self.pet = Pet.objects.create(name="Rex", species="Dog", age=5, owner=self.owner)
        self.appointment = Appointment.objects.create(date=timezone.now(), reason="Checkup", pet=self.pet)

    def test_appointment_creation(self):
        self.assertEqual(self.appointment.reason, "Checkup") # Verifica que el motivo se guarde correctamente
        self.assertEqual(self.appointment.pet.name, "Rex") # Verifica la relación con la mascota
        self.assertIsInstance(self.appointment.date, timezone.datetime) # Verifica el tipo de fecha

    def test_str_method(self):
        self.assertEqual(str(self.appointment), f"Appointment for {self.pet.name} on {self.appointment.date}")