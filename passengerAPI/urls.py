from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^passenger-registration/', views.PassengerRegistration.as_view(), name='passenger-registration'),
    url(r'^book-cab/', views.BookCab.as_view(), name='book-cab'),
]
