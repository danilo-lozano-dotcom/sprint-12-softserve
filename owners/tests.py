from django.test import TestCase
from .models import Owner

class OwnerModelTest(TestCase):

    def setUp(self):
        Owner.objects.create(name="John Doe", phone="1234567890", email="john@example.com")

    def test_owner_creation(self):
        owner = Owner.objects.get(name="John Doe")
        self.assertEqual(owner.phone, "1234567890") # Verifica que el teléfono se guarde correctamente
        self.assertEqual(owner.email, "john@example.com") # Verifica que el email se guarde correctamente

    def test_owner_str(self):
        owner = Owner.objects.get(name="John Doe")
        self.assertEqual(str(owner), "John Doe")