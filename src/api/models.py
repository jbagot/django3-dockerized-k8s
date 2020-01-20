from django.db import models


class AnimalType(models.Model):
    name = models.CharField(max_length=255)


class Animal(models.Model):
    name = models.CharField(max_length=500)
    animal_type = models.ForeignKey(to=AnimalType, on_delete=models.CASCADE)
