# Uncomment the following imports before adding the Model code
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib import admin

# Create your models here.
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    established_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name  # Return the name as the string representation

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('JEEP', 'JEEP')
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),  # Year can't be in the future
            MinValueValidator(2015)     # Year can't be earlier than 2015
        ]
    )

    def __str__(self):
        return self.name  # Return the name as the string representation

# Registering models with their respective admins
admin.site.register(CarMake)
admin.site.register(CarModel)
