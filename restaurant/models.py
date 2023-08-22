from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveBigIntegerField(validators=[MinValueValidator(1)])
    booking_date = models.DateField()

    def __str__(self):
        return f'{self.name} : {self.booking_date}'

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveBigIntegerField()
    menu_item_description = models.TextField(max_length=1000, default='')

    def __str__(self):
        return f'{self.title} : {str(self.price)}'