from django.db import models
from django.urls import reverse
import uuid
# Create your models here.
# Model 1


class CarType(models.Model):
    """Model that represents the car type"""
    car_type = models.CharField(
        max_length=200, help_text='please enter car type(e.g SUV, Salon)')

    def __str__(self):
        return self.car_type

# Model 2


class CarMake(models.Model):
    """Model that represents a car make"""
    car_make = models.CharField(
        max_length=200, help_text='please enter car make(e.g Toyota)')

    def __str__(self):
        return self.car_make

# Model 3


class CarModel(models.Model):
    """Model that rep car model"""
    """Self refers to the parent model."""
    car_model = models.CharField(
        'Model', max_length=200, help_text='please enter a car model(e.g corolla)')

    def __str__(self):
        return self.car_model


# Forth Model

class CarOwner(models.Model):
    """Model to rep car owner"""
    owner_name = models.CharField(max_length=200, help_text="enter owner name")
    manufacturer = models.CharField(
        max_length=200, help_text=" enter owner manufacturer ID")
    owner_address = models.CharField(
        max_length=200, help_text="enter owner address")
    owner_mail = models.EmailField(
        max_length=200, help_text="enter owner mail e.g abc@gmail.com")

    def __str__(self):
        return self.owner_name

# Model 5


class carInstance(models.Model):
    """Model to represent a car instance"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    car = models.ForeignKey('Car', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=500)
    due_back = models.DateField(null=True, blank=True)

    hire_status = (
        ('a', 'Available'),
        ('o', 'On loan'),
        ('r', 'Reserved'),
        ('m', 'Maintenance'),
    )

    status = models.CharField(
        max_length=1,
        choices=hire_status,
        blank=True,
        default='a',
        help_text='Car Availability'
    )

    class Meta:
        ordering = ['due_back']


# Model 6

class Car(models.Model):
    """Model that rep a car"""
    registration = models.CharField('Reg.No', max_length=7, unique=True)
    # Assign a vehicle to owner. use manufacturer number of the vehicle.
    manufacturer = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    car_type = models.ForeignKey(CarType, on_delete=models.RESTRICT)
    car_make = models.ForeignKey(CarMake, on_delete=models.RESTRICT)
    car_model = models.ForeignKey(CarModel, on_delete=models.RESTRICT)
    car_image = models.ImageField(
        upload_to='images')
    description = models.TextField(
        max_length=1000, help_text="some additional info about the car")

    """Define what the class returns"""

    def image_tag(self):
        from django.utils.html import escape
        return u'<img src="%s" />' % escape('images')
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __str__(self):
        return f'{self.registration} {self.car_make} {self.car_model} {self.car_type}'

    def get_absolute_url(self):
        # return a url to generate a detailed car record.
        return reverse('car-details', args=[str(self.id)])
