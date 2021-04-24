from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^registration/', views.DriverRegistration.as_view(), name='registration'),
    url(r'^car-own-by-driver/', views.CarOwnByDriver.as_view(), name='car-own-by-driver'),
    url(r'^ride-completed/', views.RideCompleted.as_view(), name='ride-completed'),
    url(r'^history/', views.DriverHistory.as_view(), name='history'),
]
