from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

# This connects the /accounts/ urls to the view functions
# N.B. the format <str:Parameter_Name> means that a parameter is passed in the url 
urlpatterns = [
    path('car-api', views.car_api, name ='car-api'),
    path('car-view/', views.car_view2, name ='car-view'),
    path('car-detail/<str:car_number_plate>', views.car_detail2, name ='car-detail'), 
    path('car-create/', views.car_create2, name ='car-create'),
    path('car-update/<str:car_number_plate>', views.car_update2, name ='car-update'),
    path('car-delete/<str:car_number_plate>', views.car_delete2, name ='car-delete'),

    path('booking_api', views.booking_api, name ='booking_api'),
    path('booking-view/', views.booking_view, name ='booking-view'),
    path('booking-detail/<str:pk>', views.booking_detail, name ='booking-detail'),
    path('booking-create/', views.booking_create, name ='booking-create'),
    path('booking-update/<str:pk>', views.booking_update, name ='booking-update'),
    path('booking-delete/<str:pk>', views.booking_delete, name ='booking-delete'),
    
    path('user-view/', views.user_view, name='user-view'),
    path('user-create/', views.user_create, name='user-create'),

    path('auth/', obtain_auth_token)

]