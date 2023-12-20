from django.contrib import admin
from django.urls import path
from home.views import hello_world ,nav_bar,login
urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", hello_world),
    path("nav/",nav_bar),
    path("login/",login),
]
