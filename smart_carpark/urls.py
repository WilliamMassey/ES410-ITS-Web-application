
from django.contrib import admin
from django.urls import path, include

# connect cirtain urls 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')), # home app to the base url
    path('accounts/', include('accounts.urls')) # accounts app to the /accounts/ url
]
