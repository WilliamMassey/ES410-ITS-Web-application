from django.urls import path
from . import views

# This connects the /accounts/ urls to the view functions
# N.B. the format <str:Parameter_Name> means that a parameter is passed in the url 
urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('add_booking', views.add_booking, name='add_booking'),
    path('add_car', views.add_car, name ='add_car'),

    path('car-api', views.car_api, name ='car-api'),
    path('car-view/', views.car_view, name ='car-view'),
    path('car-detail/<str:car_number_plate>', views.car_detail, name ='car-detail'), 
    path('car-create/', views.car_create, name ='car-create'),
    path('car-update/<str:car_number_plate>', views.car_update, name ='car-update'),
    path('car-delete/<str:car_number_plate>', views.car_delete, name ='car-delete'),

    path('booking_api', views.booking_api, name ='booking_api'),
    path('booking-view/', views.booking_view, name ='booking-view'),
    path('booking-detail/<str:pk>', views.booking_detail, name ='booking-detail'),
    path('booking-create/', views.booking_create, name ='booking-create'),
    path('booking-update/<str:pk>', views.booking_update, name ='booking-update'),
    path('booking-delete/<str:pk>', views.booking_delete, name ='booking-delete')

]