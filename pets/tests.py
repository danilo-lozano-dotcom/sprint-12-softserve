from django.test import TestCase
from .models import Pet, Owner

class PetModelTest(TestCase):

    def setUp(self):
        self.owner = Owner.objects.create(name="John Doe", phone="1234567890", email="john@example.com")
        self.pet = Pet.objects.create(name="Buddy", species="Dog", age=5, owner=self.owner)

    def test_pet_creation(self):
        self.assertEqual(self.pet.name, "Buddy") # Verifica que el nombre se guarde correctamente
        self.assertEqual(self.pet.species, "Dog") # Verifica la especie
        self.assertEqual(self.pet.age, 5) # Verifica la edad
        self.assertEqual(self.pet.owner, self.owner) # Verifica la relación con el propietario

    def test_pet_str(self):
        self.assertEqual(str(self.pet), "Buddy")