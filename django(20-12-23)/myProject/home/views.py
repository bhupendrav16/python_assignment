from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
weeksDays = ["Monday" , "Tuesday"]
links_name = ["Google","youtube"]
link_ref = ["https://www.google.com" , "https://www.youtube.com"]
def hello_world(request):
    print("req")
    print(request)
    return HttpResponse('hello')

def nav_bar(request):
    return render(request, "home/home.html")

def login(request):
    return render( request , 'home/login.html', {"name" : links_name ,"link_r":link_ref} )
