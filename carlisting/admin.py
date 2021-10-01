from django.contrib import admin

# Register your models here.
from .models import CarOwner, CarType, CarModel, CarMake, Car, carInstance

admin.site.register(CarType)
admin.site.register(CarMake)
admin.site.register(CarModel)
admin.site.register(Car)
admin.site.register(carInstance)
admin.site.register(CarOwner)
fields = ( 'image_tag', )
readonly_fields = ('image_tag',)