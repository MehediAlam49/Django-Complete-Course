from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Welcome to Home Page')

def student_list(request):
    return HttpResponse('All student list')

def contact(request):
    return HttpResponse('Contact page')