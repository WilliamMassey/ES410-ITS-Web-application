from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('add_booking', views.add_booking, name='add_booking'),
    path('add_car', views.add_car, name ='add_car')
]