from django.urls import path
from courses.views import *


urlpatterns = [
    path('', home, name='home'),
    path('list/', course_list, name='course-list')
]
