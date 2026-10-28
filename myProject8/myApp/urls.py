from django.urls import path
from myApp.views import *

urlpatterns = [
    path('', home, name='home'),
    path('course/', course, name='course'),
]
