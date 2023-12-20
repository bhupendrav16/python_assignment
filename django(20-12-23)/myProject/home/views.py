from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello_world(request):
    print("req")
    print(request)
    return HttpResponse('hello')

def nav_bar(request):
    return render(request, "home/home.html")

def login(request):
    return render( request , 'home/login.html')