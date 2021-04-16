from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse

# Importing models from accounts app
from .models import Car, User_Car_Mapping, Booking
# importing carpark model from home model 
from home.models  import Carpark
from django.contrib.auth.models import User

from .func import conv_html_datetime # importing function used to 
from datetime import datetime, timedelta

#rest framework imports
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

#importing accounts serializers 
from .serializers import CarSerializer, BookingSerializer, UserSerializer 

# is_car_user_mapped checks whether a mapping exists between the given user and the car with the given car numberplate. If it is mapped, a tupple is returned with the first element stating whether they are mapped and the second is the mapping. if not mapped the first element is given as false, and the second element is a response object, stating what the issue is.  
def is_car_user_mapped(user, car_number_plate):
    try:
        user_car_mapping = User_Car_Mapping.objects.get(user = user, car__car_number_plate = car_number_plate)
    except User_Car_Mapping.DoesNotExist:
        return False, Response("ERROR: CURRENT USER IS NOT MAPPED TO THE CAR WITH NUMBERPLATE " + car_number_plate)
    except User_Car_Mapping.MultipleObjectsReturned:
        return False, Response("ERROR: MULTIPLE MAPPINGS EXIST BETWEEN THE CURRENT USER AND THE CAR WITH NUMBERPLATE " + car_number_plate)
    
    return True, user_car_mapping

@api_view(['GET'])
def user_view(request):
    users = User.objects.all()

    serializer = UserSerializer(data=users, many = True)
    serializer.is_valid() 
    return Response(serializer.data)

@api_view(['POST'])
def user_create(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        print(serializer.validated_data)
        user = serializer.create(serializer.validated_data)
        return Response(serializer.data)
    else: 
        return Response(serializer.errors)



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
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def car_view2(request):
    print(request)
    user  = request.user
    numberplateQS = User_Car_Mapping.objects.filter(user__exact = request.user)  
    numberplates = numberplateQS.values_list('car', flat = True) 
    cars = Car.objects.filter(car_number_plate__in = numberplates) 
    serializer = CarSerializer(data = cars, many = True)
    serializer.is_valid()
    print(serializer.data)
    return Response(serializer.data)




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
        return Response("ERROR: YOU ARE NOT LOGGED IN") # if the user isn't authenticated return error message

# car_detail returns the serialized car object of the car with the numberplate given as the parameter "car_number_plate"
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def car_detail2(request, car_number_plate):

    (is_mapped, result) = is_car_user_mapped(request.user, car_number_plate) 
    if is_mapped: 
        user_car_mapping = result
    else: 
        return result

    car = user_car_mapping.car
    serializer = CarSerializer(car, many = False) 
    return Response(serializer.data)
   

@api_view(['GET'])
def car_detail(request, car_number_plate):
    if request.user.is_authenticated: # check if the user is authenticated
        (is_mapped, result) = is_car_user_mapped(request.user, car_number_plate) # determine whether user and inputted car are mapped
        if is_mapped: # if mapped, set user_car_mapping to the appropriate UCM
            user_car_mapping = result
        else: # if not mapped return the corresponding error message
            return result

        car = user_car_mapping.car # get the car from UCM
        serializer = CarSerializer(car, many = False) # serialize car
        return Response(serializer.data) # return serialized car
    else:
        return Response("ERROR: YOU ARE NOT LOGGED IN") # if the user isn't authenticated return error message

# car_create takes serialized car data and saves car object to database
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def car_create2(request):
    serializer = CarSerializer(data = request.data) 
    if serializer.is_valid():
        car = serializer.create(serializer.validated_data) 
        mapping = User_Car_Mapping(car = car, user = request.user) 
        mapping.save() 
        return Response(serializer.data)
    elif "car with this car number plate already exists." in serializer.errors['car_number_plate'] and len(serializer.errors['car_number_plate'])==1:
        car = Car.objects.get(car_number_plate = serializer.data['car_number_plate'])
        (is_mapped, result) = is_car_user_mapped(request.user, car.car_number_plate)
        print(is_mapped)
        print(result)
        if is_mapped:
            return Response("The car is already mapped")
        else: 
            user_car_mapping = User_Car_Mapping.objects.create(car = car, user = request.user)
            return Response(f"the car with numberplate {car.car_number_plate} already exists, the user {request.user} is now mapped to it")
    else: 
        return Response(serializer.errors)


@api_view(['POST'])
def car_create(request):
    if request.user.is_authenticated: # if user is authenticated 
        serializer = CarSerializer(data = request.data) # get a serializer object from data
        if serializer.is_valid(): # is the data recived valid
            car = serializer.create(serializer.validated_data) # save the Car object from serializer and set that object to car
            mapping = User_Car_Mapping(car = car, user = request.user) # create the UCM using the current user and the car just created
            mapping.save() # save the UCM
            return Response(serializer.data) # return the serialized object
        elif "car with this car number plate already exists." in serializer.errors['car_number_plate'] and len(serializer.errors['car_number_plate'])==1:
            car = Car.objects.get(car_number_plate = serializer.data['car_number_plate'])
            (is_mapped, result) = is_car_user_mapped(request.user, car.car_number_plate)
            print(is_mapped)
            print(result)
            if is_mapped:
                return Response("The car is already mapped")
            else: 
                user_car_mapping = User_Car_Mapping.objects.create(car = car, user = request.user)
                return Response(f"the car with numberplate {car.car_number_plate} already exists, the user {request.user} is now mapped to it")
        else: 
            return Response(serializer.errors) # return the error response, outlining, what was wrong with the serialized data 
    else:
        return Response("ERROR: YOU ARE NOT LOGGED IN") # if the user isn't authenticated return error message
    
# car_update changes the attributes of the car with the numberplate given as the parameter "car_number_plate" 
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def car_update2(request, car_number_plate): 
    (is_mapped, result) = is_car_user_mapped(request.user, car_number_plate) 
    if is_mapped:
        user_car_mapping = result
    else: 
        return result

    car = user_car_mapping.car 
    serializer = CarSerializer(instance = car,data = request.data) 
    if serializer.is_valid():
        serializer.save() 
        return Response(serializer.validated_data) 
    else:
            return Response(serializer.errors) 



@api_view(['POST'])
def car_update(request, car_number_plate): 
    if request.user.is_authenticated: # check if user is authenticated 
        # check if user is mapped to car
        (is_mapped, result) = is_car_user_mapped(request.user, car_number_plate) # idential useage as found in car_detail (lines 68-72)
        if is_mapped:
            user_car_mapping = result
        else: 
            return result

        car = user_car_mapping.car # get the car from UCM
        
        serializer = CarSerializer(instance = car,data = request.data) # This functions the same as in car_create(), however the argument instance means that will change a current object rather than creating a new one
        if serializer.is_valid(): # is the data recived valid

            serializer.save() # update car object with new attributes
            return Response(serializer.validated_data) # return new car object
        else:
                return Response(serializer.errors) # return errors of serialized object
    else:
        return Response("ERROR: YOU ARE NOT LOGGED IN")

# car_delete deletes the car with the numberplate given as the parameter "car_number_plate"
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def car_delete2(request, car_number_plate):
    (is_mapped, result) = is_car_user_mapped(request.user, car_number_plate) 
    if is_mapped:
        user_car_mapping = result
    else: 
        return result
    other_mappings =  len(list(User_Car_Mapping.objects.filter(car = car_number_plate)))
    print(other_mappings)
    ### Need to add functionality that if there are more than one mappings associated with a single car, that the current users mapping is deleted rather than the car itself
    
    no_other_mappings =  len(list(User_Car_Mapping.objects.filter(car = car_number_plate)))
    if no_other_mappings == 1:
        car = user_car_mapping.car # get the car from UCM
        car.delete() # delete the car object
        return Response("THE CAR AND MAPPING WERE SUCCESSFULLY DELETED") # infrom frontend the car was successfully deleted
    else:
        user_car_mapping.delete()
        return Response("THE USER_CAR_MAPPING WAS SUCCESSFULLY DELETED") # infrom frontend the car was successfully deleted

@api_view(['DELETE'])
def car_delete(request, car_number_plate):
    if request.user.is_authenticated: # check if user is logged in 
        
        # check if user is mapped to car
        (is_mapped, result) = is_car_user_mapped(request.user, car_number_plate) # idential useage as found in car_detail (lines 68-72)
        if is_mapped:
            user_car_mapping = result
        else: 
            return result
        ### Need to add functionality that if there are more than one mappings associated with a single car, that the current users mapping is deleted rather than the car itself
        no_other_mappings =  len(list(User_Car_Mapping.objects.filter(car = car_number_plate)))
        if no_other_mappings == 1:
            car = user_car_mapping.car # get the car from UCM
            car.delete() # delete the car object
            return Response("THE CAR AND MAPPING WERE SUCCESSFULLY DELETED") # infrom frontend the car was successfully deleted
        else:
            user_car_mapping.delete()
            return Response("THE USER_CAR_MAPPING WAS SUCCESSFULLY DELETED") # infrom frontend the car was successfully deleted

    else: 
        return Response("ERROR: YOU ARE NOT LOGGED IN")


### Booking API ###
# booking_api returns a list of the valid urls and the required format for the booking api 
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

# booking_detail does the equivalent to car_api
@api_view(['GET'])
def booking_view(request):
    if request.user.is_authenticated: # check if user is authenticated 
        bookings = (Booking.objects.filter(user__exact = request.user)) # gets all bookings associated with current user
        serializer = BookingSerializer(data = bookings, many = True) # Serializes all the bookings 
        serializer.is_valid() # check is valid
        return Response(serializer.data) # return serialized data
    else:
        return Response("ERROR: YOU ARE NOT LOGGED IN")

# booking_detail does the equivalent to car_detail 
@api_view(['GET'])
def booking_detail(request, pk):
    if request.user.is_authenticated: # check if user is authenticated 
        
        try: # check whether the booking with id = pk exists and that the current user is associated to thatvbooking 
            booking = Booking.objects.get(user = request.user, id = pk)
        except Booking.DoesNotExist:
            return Response("ERROR: CURRENT USER HAS NO BOOKING WITH ID " +str(pk))

        serializer = BookingSerializer(booking, many = False) # serialize the booking
        
        return Response(serializer.data) # return serialized data  
    else:
        return Response("ERROR: YOU ARE NOT LOGGED IN") 

# booking_create does the equivalent to car_create 
@api_view(['POST'])
def booking_create(request):
    if request.user.is_authenticated: # check if the user authenticated
        serializer = BookingSerializer(data = request.data) # serialize the booking from data 
        if serializer.is_valid(): # check if data is valid

            # Get the data from serializer
            car = serializer.validated_data['car']
            carpark = serializer.validated_data['carpark']
            start_datetime = serializer.validated_data['start_datetime']
            end_datetime = serializer.validated_data['end_datetime']

            ### Checking whether data recived passes additional restrictions
            # determine whether user been mapped to the car
            (is_mapped, result) = is_car_user_mapped(request.user, car.car_number_plate)
            if not is_mapped:
                return result                
            
            # add addtional restrictions datetime validity, 
            
            serializer.save() # save the serializer 
            return Response(serializer.data) # return serialized data to confirm 
        else:
            return Response(serializer.errors)
    else:
        return Response("ERROR: YOU ARE NOT LOGGED IN")
    
# booking_update does the equivalent to car_update 
@api_view(['POST'])
def booking_update(request, pk):
    if request.user.is_authenticated:
        
        try: # check if a booking that matches the id, pk
            booking = Booking.objects.get(id = pk)
        except Booking.DoesNotExist:
            return Response("ERROR: NO BOOKING WITH ID " +str(pk) +" EXISTS")

        if booking.user != request.user: # check if the user assoicated with that booking is the curretn user
            return Response("ERROR: THE BOOKING WITH ID " +str(pk) + " DOESN'T BELONG TO THE CURRENT USER")
        
        serializer = BookingSerializer(instance = booking, data = request.data) # create serializer updating the booking 

        if serializer.is_valid(): # check if the serializer is valid
            # get data from serializer
            user = serializer.validated_data['user']
            car = serializer.validated_data['car']
            carpark = serializer.validated_data['carpark']
            start_datetime = serializer.validated_data['start_datetime']
            end_datetime = serializer.validated_data['end_datetime']

            ### Checking whether data recived passes additional restrictions
            # determine whether user been mapped to the car 
            (is_mapped, result) = is_car_user_mapped(request.user, car.car_number_plate)
            if not is_mapped:
                return result 
            
            # add addtional restrictions datetime validity, 
            
            serializer.save() # save serialized data
            return Response(serializer.data) # return updated serialized data as confirmation
        else:
            return Response(serializer.errors)
    else:
        return Response("ERROR: YOU ARE NOT LOGGED IN")

# booking_delete does the equivalent to car_delete 
@api_view(['DELETE'])
def booking_delete(request, pk):
    if request.user.is_authenticated: # check if user is authenticated 
        # check a booking with the id "pk" exists
        try:
            booking = Booking.ojbects.get(id = pk)
        except DoesNotExist:
            return Response("Booking doesn't exist")
        booking_user = booking.user 
        if booking_user != request.user: # check whether the booking is associated with the current user
            return Response("ERROR: You do no have acess to this booking")
        
        booking.delete() # delete the booking
        return Response("booking id " + str(pk) + " has been successfully deleted") # return message stating that it has been successfully deleted
    else: 
        return Response("ERROR: YOU ARE NOT LOGGED IN")
