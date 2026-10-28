from django.urls import path
from students.views import *


urlpatterns = [
    path('', home, name='home'),
    path('student-list/', student_list, name='student_list'),
    path('contact/', contact, name='contact'),
]
