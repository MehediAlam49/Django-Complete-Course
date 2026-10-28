from django.urls import path
from myApp.views import home,course

urlpatterns = [
    path('student/<int:id>', home, name='home'),
    path('course/', course, name='course'),
]
