from django.db import models
from owners.models import Owner

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.species})"