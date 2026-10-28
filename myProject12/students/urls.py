from django.urls import path
from students.views import *

urlpatterns = [
    path('', home, name='home'),
    path('list/', student_list, name='student-list'),
]
