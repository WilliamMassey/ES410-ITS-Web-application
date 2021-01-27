from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('email_test', views.email_test, name = 'email_test')
]