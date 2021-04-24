from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^driver-registration/', views.DriverRegistration.as_view(), name='driver-registration'),
    url(r'^car-own-by-driver/', views.CarOwnByDriver.as_view(), name='car-own-by-driver'),
]
