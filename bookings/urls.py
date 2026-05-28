from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:track_pk>/', views.booking_create, name='booking_create'),
    path('my', views.my_bookings, name='my_bookings'),
]