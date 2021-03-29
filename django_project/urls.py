from django.contrib import admin
from django.urls import path
from planner.views import home, checkweather, addtodo, showtodo, search, deletetask
from auapp.views import usignup, ulogin, ulogout, index, fp
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('home/',home, name='home'),
    path('usignup/', usignup, name='usignup'),
    path('ulogin/', ulogin, name='ulogin'),
    path('ulogout/', ulogout, name='ulogout'),
    path('checkweather/', checkweather, name='checkweather'),
    path('addtodo/', addtodo, name='addtodo'),
    path('showtodo/', showtodo, name='showtodo'),
    path('search/', search, name='search'),
    path('fp/', fp, name='fp'),
    path('deletetask/<int:id>', deletetask, name='deletetask'),
]