from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^registration/', views.PassengerRegistration.as_view(), name='registration'),
    url(r'^book-cab/', views.BookCab.as_view(), name='book-cab'),
    url(r'^history/', views.PassengerHistory.as_view(), name='history'),
]
