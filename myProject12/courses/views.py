from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Couse Home page')

def course_list(request):
    return HttpResponse('Course List')