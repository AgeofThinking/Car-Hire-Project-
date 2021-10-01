from django.shortcuts import render, redirect
from django.http import HttpResponse, request, response
from .models import carInstance, Car
from .forms import *
from django.views.generic import ListView
# Create your views here.


def index(request):
    """View function to specify the site hompage"""

    # generate a count of all the cars in the system'
    cars_count = Car.objects.all().count()
    car_instance_count = carInstance.objects.all().count()

    # count the number of available cars
    num_cars_available = carInstance.objects.filter(status__exact='a').count()

    number_of_visits = request.session.get('number_of_visits', 0)
    request.session['number_of_visits'] = number_of_visits + 1

    # Context Specifies how the data will be presented in the rendered view
    context = {
        'cars_count': cars_count,
        'num_cars_available': num_cars_available,
        'car_instance_count': car_instance_count,
        'number_of_visits': number_of_visits,
        

    }

    # Render a HTML file, index.html containing the data in the context
    return render(request, 'index.html', context=context)


# Create your views here.
def hotel_image_view(request):

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageForm()
    return render(request, 'image_form.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')
# views for templates


def list_cars(request):
    cars = Car.objects.all()
    return render(request, 'cars.html', {'cars': cars})


def car(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'car.html', {'car': car})
