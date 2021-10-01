# map urls for ur view functions here

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# URLConf
urlpatterns = [
    path('', views.index, name='home'),
    path('cars/', views.list_cars, name='list-cars'),
    path('cars/<int:car_id>/details', views.car, name='car-details'),
    # path('details/', views.car_details),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)