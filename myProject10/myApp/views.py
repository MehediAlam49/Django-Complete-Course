from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request, id):
    return HttpResponse(f'Student ID: {id}')

def course(request):
    name=request.GET.get('name', 'Django')
    method=request.method
    return HttpResponse(f'{method} : {name}')