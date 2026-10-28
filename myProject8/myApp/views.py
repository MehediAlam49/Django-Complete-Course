from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse(
        "Welcome to myApp"
    )

def course(request):
    name = request.GET.get("name", "Django")
    method = request.method
    return HttpResponse(f"{method}: {name}")
