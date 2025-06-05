# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f'CarMake(Name: {name}, Description: {description})'


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

TYPE_CHOICES = {
    'SEDAN': "Sedan",
    'SUV': "SUV",
    'WAGON': "Wagon"
}

class CarModel(models.Model):
    name = models.CharField(max_length=30)
    dealerId = models.IntegerField()
    carType = models.CharField(choices=TYPE_CHOICES)
    year = models.IntegerField()
    carMake = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    def __str__(self):
        return f'CarModel(Name: {name}, Dealer: {dealerId}, CarType: {carType}, Year: {year}, CarMake:{carMake})'