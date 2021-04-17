from django.shortcuts import render, redirect
from .models import Carpark, Live_Feed, Carpark_Data
from accounts.models import User_Car_Mapping, Car, Booking
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from datetime import datetime, timedelta, time, date


