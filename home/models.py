from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank= True, null= True)

    # def __str__(self):
    #     return self.name

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    # Add more fields as needed (e.g., mileage, price, etc.)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
