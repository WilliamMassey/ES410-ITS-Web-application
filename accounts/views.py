from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse

# Importing models from accounts app
from .models import Car, User_Car_Mapping, Booking
# importing carpark model from home model 
from home.models  import Carpark

from .func import conv_html_datetime # importing function used to 
from datetime import datetime, timedelta

#rest framework imports
from rest_framework.decorators import api_view
from rest_framework.response import Response

#importing accounts serializers 
from .serializers import CarSerializer, BookingSerializer


def is_car_user_mapped(request, car_number_plate):
    try:
        user_car_mapping = User_Car_Mapping.objects.get(user = request.user, car__car_number_plate = car_number_plate)
    except User_Car_Mapping.DoesNotExist:
        return False, Response("ERROR: CURRENT USER IS NOT MAPPED TO THE CAR WITH NUMBERPLATE " + car_number_plate)
    except User_Car_Mapping.MultipleObjectsReturned:
        return False, Response("ERROR: MULTIPLE MAPPINGS EXIST BETWEEN THE CURRENT USER AND THE CAR WITH NUMBERPLATE " + car_number_plate)
    
    return True, user_car_mapping

##### APIs #####
## Notes
# 1) All api functions have the decorator @api_view([list_of_methods]), as described in REST API documentation, where list of methods is a list of the HTTP methods that the function can use, either "GET", "POST" or "DELETE"
# 2) All responses with "ERROR: ..." are placeholders for debugging purposes, and will be replaced with a more formalised error system
# 3) UCM is short hand for the model User_Car_Mapping
### CAR API ###
# car_api returns a list of the valid urls and the required format for the car api 
@api_view(['GET'])
def car_api(request):
    api_urls = {
        'View': '/car-view/',
        'Detail': '/car-detail/<str:car_number_plate>/',
        'Create': '/car-create/',
        'Update': '/car-update/<str:car_number_plate>/',
        'Delete': '/car-delete/<str:car_number_plate>/',
    }
    return Response(api_urls)

# car_view returns a serialized list of all of the cars that the current user has registered
@api_view(['GET']) 
def car_view(request):
    if request.user.is_authenticated: # check if the user is authenticated
        numberplateQS = User_Car_Mapping.objects.filter(user__exact = request.user) # Query set of all UCMs of current user  
        numberplates = numberplateQS.values_list('car', flat = True) # make a list containing the numberplates of all the cars from UCM query set
        cars = Car.objects.filter(car_number_plate__in = numberplates) # use the number plates to get a query set of the cars registerd to the user 
        
        serializer = CarSerializer(data = cars, many = True) # serialize the query set 
        serializer.is_valid() # validate the data
        return Response(serializer.data) # return the serialized data using the "Response" function
    else:
        return Response("ERROR: YOU ARE NOT LOGGED IN") 

# car_detail returns the serialized car object of the car with the numberplate "car_number_plate"
@api_view(['GET'])
def car_detail(request, car_number_plate):
    if request.user.is_authenticated: # check if the user is authenticated
        (is_mapped, result) = is_car_user_mapped(request, car_number_plate)
        if is_mapped:
            user_car_mapping = result
        else: 
            return result

        car = user_car_mapping.car
        serializer = CarSerializer(car, many = False) 
        return Response(serializer.data) # return serialized car
    else:
        return Response("ERROR: YOU ARE NOT LOGGED IN") # if the user isn't authenticated return standing error message

@api_view(['POST'])
def car_create(request):
    if request.user.is_authenticated: # if user is authenticated 
        serializer = CarSerializer(data = request.data) # get a serializer object from data
        if serializer.is_valid(): 
            car = serializer.create(serializer.validated_data) 
            mapping = User_Car_Mapping(car = car, user = request.user) # create the UCM using the currently logged in user and the car created
            mapping.save() # save the UCM
            return Response(serializer.data) # return the serialized object, as confirmation  
        else: 
            return Response(serializer.errors) # return the error response, outlining, what was wrong iwtht he serialized data 
    else:
        return Response("ERROR: YOU ARE NOT LOGGED IN")
    
# car_update function, uses the identical flow of car_create, however rather than using the save method on the serializer, getting the car object using the number plate then updating it. 
@api_view(['POST'])
def car_update(request, car_number_plate): 
    if request.user.is_authenticated:

        (is_mapped, result) = is_car_user_mapped(request, car_number_plate)
        if is_mapped:
            user_car_mapping = result
        else: 
            return result

        car = user_car_mapping.car
        
        serializer = CarSerializer(instance = car,data = request.data)
        if serializer.is_valid():

            serializer.save()
            print("serializer was valid")
            return Response(serializer.data)
        else:
                return Response(serializer.errors)
    else:
        return Response("ERROR: YOU ARE NOT LOGGED IN")


@api_view(['DELETE'])
def car_delete(request, car_number_plate):
    if request.user.is_authenticated:
        
        (is_mapped, result) = is_car_user_mapped(request, car_number_plate)
        if is_mapped:
            user_car_mapping = result
        else: 
            return result

        car = user_car_mapping.car
        car.delete()
        return Response("THE CAR WAS SUCCESSFULLY DELETED")

    else: 
        return Response("ERROR: YOU ARE NOT LOGGED IN")


### Booking API ###
@api_view(['GET'])
def booking_api(request):
    api_urls = {
        'View': '/booking-view/',
        'Detail': '/booking-detail/<str:pk>/',
        'Create': '/booking-create/',
        'Update': '/booking-update/<str:pk>/',
        'Delete': '/booking-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def booking_view(request):
    if request.user.is_authenticated:
        
        bookings = (Booking.objects.filter(user__exact = request.user))
        print("bookings " + str(bookings))
        serializer = BookingSerializer(data = bookings, many = True)
        serializer.is_valid()
        # if empty do what? or easier to do on front end
        return Response(serializer.data)
    else:
        return Response("ERROR: YOU ARE NOT LOGGED IN")

@api_view(['GET'])
def booking_detail(request, pk):
    if request.user.is_authenticated:

        try:
            booking = Booking.objects.get(user = request.user, id = pk)
        except Booking.DoesNotExist:
            return Response("ERROR: CURRENT USER HAS NO BOOKING WITH ID " +str(pk))

        serializer = BookingSerializer(booking, many = False)
        
        print(serializer.data)
        # if empty do what? or easier to do on front end
        return Response(serializer.data)
    else:
        return Response("ERROR: YOU ARE NOT LOGGED IN")

@api_view(['POST'])
def booking_create(request):
    if request.user.is_authenticated:
        serializer = BookingSerializer(data = request.data)
        if serializer.is_valid():

            car = serializer.validated_data['car']
            carpark = serializer.validated_data['carpark']
            start_datetime = serializer.validated_data['start_datetime']
            end_datetime = serializer.validated_data['end_datetime']

            ### Checking whether data recived passes additional restrictions
            # determine whether user been mapped to the car
            try:
                user_car_mapping = User_Car_Mapping.objects.get(user__exact = request.user, car = car)
            except User_Car_Mapping.DoesNotExist:
                return Response("ERROR: CURRENT OWNER HAS NOT BEEN MAPPED ONTO THE CAR")
            except User_Car_Mapping.MultipleObjectsReturned:
                return Response("ERROR: DUPLICATE MAPPINGS BETWEEN USER AND CAR EXIST")
            
            # add addtional restrictions datetime validity, 
            
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    else:
        return Response("ERROR: YOU ARE NOT LOGGED IN")
    

@api_view(['POST'])
def booking_update(request, pk):
    if request.user.is_authenticated:

        try:
            booking = Booking.objects.get(id = pk)
        except Booking.DoesNotExist:
            return Response("ERROR: NO BOOKING WITH ID " +str(pk) +" EXISTS")

        if booking.user != request.user:
            return Response("ERROR: THE BOOKING WITH ID " +str(pk) + " DOESN'T BELONG TO THE CURRENT USER")
        
        serializer = BookingSerializer(instance = booking, data = request.data)

        if serializer.is_valid():
            user = serializer.validated_data['user']
            car = serializer.validated_data['car']
            carpark = serializer.validated_data['carpark']
            start_datetime = serializer.validated_data['start_datetime']
            end_datetime = serializer.validated_data['end_datetime']

            ### Checking whether data recived passes additional restrictions
            # determine whether user been mapped to the car 
            try:
                user_car_mapping = User_Car_Mapping.objects.get(user__exact = request.user, car = car)
            except User_Car_Mapping.DoesNotExist:
                return Response("ERROR: CURRENT OWNER HAS NOT BEEN MAPPED ONTO THE CAR")
            except User_Car_Mapping.MultipleObjectsReturned:
                return Response("ERROR: DUPLICATE MAPPINGS BETWEEN USER AND CAR EXIST")
            
            # add addtional restrictions datetime validity, 
            
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    else:
        return Response("ERROR: YOU ARE NOT LOGGED IN")


@api_view(['DELETE'])
def booking_delete(request, pk):
    if request.user.is_authenticated:
        try:
            booking = Booking.ojbects.get(id = pk)
        except DoesNotExist:
            return Response("Booking doesn't exist")
        booking_user = booking.user
        if booking_user != request.user:
            return Response("ERROR: You do no have acess to this booking")
        
        booking.delete()
        return Response("booking id " + str(pk) + " has been successfully deleted")
    else: 
        return Response("ERROR: YOU ARE NOT LOGGED IN")




def accounts(request):

    #by default login 
    return render(request, 'login.html')

def login(request):
    ### ADD EMAIL CONFIRMED ###
    if request.method == 'POST':
        uni_id = request.POST['uni_id']
        password = request.POST['password']
        
        user = auth.authenticate(username = uni_id, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'The details entered do not exist.')
            return redirect('login')

    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        uni_id = request.POST['uni_id']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        email = request.POST['email']
        email_confirm = request.POST['email_confirm']

        ###### CONDITOINS ######
        ### NAMES ###
        name_valid = True
        # are the names blank
        if (not first_name) or (not last_name):
            messages.info(request, "The names can't be left blank.", extra_tags='names')
            name_valid = False
        ### only spaces ###

        ### UNI-ID ###
        uni_id_valid = True
        # uni_id length
        if len(uni_id) != 8:
            messages.info(request, 'University ID is 8 charaters long.', extra_tags='uni_id')
            uni_id_valid = False
            
        # uni id take
        if User.objects.filter(username = uni_id).exists():
            messages.info(request, 'This university Id is already in use.', extra_tags='uni_id')
            uni_id_valid = False
        ### add valid uni ID ###

        ### PASSWORDS ###
        password_valid = True
        # passwords match
        if password!= password_confirm:
            messages.info(request,"The passwords don't match.", extra_tags='password')
            password_valid = False

        # password not too short
        if len(password) <7:
            messages.info(request, "The password needs to be at least 7 charaters long.", extra_tags='password')
            password_valid = False
        ### passwords contain cirtain charaters ###

        ### EMAILS ###
        email_valid = True
        # emails match
        if email != email_confirm:
            messages.info(request, "The emails given don't match.", extra_tags='email')
            email_valid = False
            
        # email not taken
        if User.objects.filter(email = email).exists():
            messages.info(request, 'This email has already been taken.', extra_tags='email')
            email_valid = False

        ###### CHECK CONDITIONS ######
        if name_valid and uni_id_valid and password_valid and email_valid:
            user = User.objects.create_user(username=uni_id, password=password, email=email,first_name=first_name,last_name=last_name)
            user.save()
            print("user created")
            return redirect("/")
        else:
            return redirect('register')
    #by default login 
    else:
        return render(request, 'register.html')

def add_car(request):
    if request.user.is_authenticated == True:
        if request.method == 'POST':
            car_number_plate =  request.POST['car_number_plate']
            car_number_plate_confirmation = request.POST['car_number_plate_confirmation']
            manufacturer = request.POST['manufacturer']
            car_colour = request.POST['car_colour']

            car_number_plate_is_valid = True
            car_colour_is_valid = True
            manufacturer_is_valid = True
            ###### CONDITIONS ######

            ### NUMBER PLATE ###
            if len(car_number_plate) > 8:
                car_number_plate_is_valid = False
                messages.info(request, 'Car number plate is too long.', extra_tags = 'car_number_plate')

            if len(car_number_plate) == 0:
                car_number_plate_is_valid = False
                messages.info(request, "Don't leave the car number plate field blank.", extra_tags = 'car_number_plate')

            if Car.objects.filter(car_number_plate = car_number_plate).exists():
                messages.info(request,'This car has already been registered', extra_tags = 'car_number_plate')
                car_number_plate_is_valid = False

            if car_number_plate != car_number_plate_confirmation:
                messages.info(request, "The number plates added don't match")
                car_number_plate_is_valid = False
            

            ### MANUFACTURER ###
            if len(manufacturer) == 0:
                car_number_plate_is_valid = False
                messages.info(request, "Don't leave the manufacturer field blank.", extra_tags = 'manufacturer')


            ### CAR COLOUR ###
            if car_colour == 'x':
                car_colour_is_valid = False
                messages.info(request, 'Please select a car colour.', extra_tags='car_colour')                

            car_number_plate = car_number_plate.upper()
            ###### CHECK CONDITIONS ######
            if car_number_plate_is_valid and manufacturer_is_valid and car_colour_is_valid:
                # CREATE car and user_car_mapping objects
                new_car = Car(car_number_plate=car_number_plate, colour = car_colour, manufacturer = manufacturer)
                
                mapping = User_Car_Mapping(car = new_car, user = request.user)

                new_car.save()
                mapping.save()
                print("all fields valid, car and mapping added")
                return redirect('/')
            else:
                print("some fields are in valid redirect to add_car")
                return redirect('add_car')
        else:
            print("first visit to add car rendering page")
            return render(request, 'add_car.html')
    else: 
        print("not logged in go to login page")
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def add_booking(request):
    if request.user.is_authenticated == True:
        if request.method == 'POST':
            user = request.user
            car_number_plate =  request.POST['car']
            start_datetime_str = request.POST['start_datetime']
            end_datetime_str = request.POST['end_datetime']
            carpark = request.POST['carpark']

            # setting criteria as true
            car_is_valid = True
            start_datetime_is_valid = True
            end_datetime_is_valid = True
            carpark_is_valid = True
            
            ###### REFROMAT DATETIMES ######
            # maximum difference between start and end
            max_diff = timedelta(days=2)
            
            start_datetime = conv_html_datetime(start_datetime_str)
            end_datetime = conv_html_datetime(end_datetime_str)
            
            ###### Conditions ######
            ### ADD BOOKING COLISSION CHECK ###
            ### START DATE ###
            # field is empty
            if not start_datetime:
                start_datetime_is_valid = False
                messages.info(request, "Don't leave the start date or time blank.", extra_tags='start_datetime')

            # before current date
            if datetime.today().date() > start_datetime.date():
                start_datetime_is_valid = False
                messages.info(request, 'The date selected is before today.', extra_tags='start_datetime')

            # today but before current time 
            if datetime.now().time() > start_datetime.time() and datetime.today().date() == start_datetime.date():
                start_datetime_is_valid = False
                messages.info(request, 'The time selected is before now.', extra_tags='start_datetime')

            # date is 1/1/2000 
            if start_datetime == datetime(2000,1,1):
                messages.info(request, 'A fault has occoured or you have entered the date 1/1/2000', extra_tags='start_datetime')
                start_datetime_is_valid = False

            ### END DATE ###
            # field is empty
            if not end_datetime:
                end_datetime_is_valid = False
                messages.info(request, "Don't leave the end date or time blank.", extra_tags='end_datetime')

            # today but before current time 
            if datetime.now().time() > end_datetime.time() and datetime.today().date() == end_datetime.date():
                end_datetime_is_valid = False
                messages.info(request, 'The time selected is before now.', extra_tags='end_datetime')

            # before current date
            if datetime.today().date() > end_datetime.date():
                end_datetime_is_valid = False
                messages.info(request, 'The date or time selected is before today.', extra_tags='end_datetime')

            # start and end are far apart
            if (end_datetime - start_datetime) > max_diff:
                end_datetime_is_valid = False
                messages.info(request, 'The length of the booking is too long.')

            # date is 1/1/2000 
            if end_datetime == datetime(2000,1,1):
                messages.info(request, 'A fault has occoured or you have entered the date 1/1/2000', extra_tags='end_datetime')
                end_datetime_is_valid = False


            ### CARPARK ###
            # field is empty
            if carpark == 'x':
                carpark_is_valid = False
                messages.info(request, "Don't leave the carpark field blank.", extra_tags='carpark')
                
            ### CAR ###
            # field is empty
            if car_number_plate == 'x':
                car_is_valid = False
                messages.info(request, "Don't leave the car field blank.", extra_tags='car')

            ###### CHECK CONDITIONS ######
            if car_is_valid and carpark_is_valid and end_datetime_is_valid and start_datetime_is_valid:
                print("booking fields entered correctly sending to home")
                car = Car.objects.get(car_number_plate__exact = car_number_plate)
                carpark_obj = Carpark.objects.get(name__exact = carpark)
                Booking.objects.create(user = user, car = car, start_datetime = start_datetime, end_datetime = end_datetime, carpark = carpark_obj)
                return redirect('/')
                
            else:
                print("booking fields entered incorrectly returning to booking")
                return redirect('add_booking')
        else:
            cars = list(User_Car_Mapping.objects.filter(user = request.user).values_list('car', flat=True))
            #print("From add_Bookings page "+str(cars))
            carparks = Carpark.objects.all()
            print("Carparks " + str(carparks))
            return render(request, 'add_booking.html', {'cars' : cars, 'carparks': carparks})
    else:
        redirect('/')
