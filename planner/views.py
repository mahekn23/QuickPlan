from django.shortcuts import render, redirect
from .models import TodoModel
from .forms import TodoForm
from django.contrib.auth.models import User
import requests
import datetime
import sqlite3
from sqlite3 import Error
# Create your views here.
def home(request):
	if request.user.is_authenticated:
		return render(request, 'home.html')
	else:
		return redirect('ulogin')
def checkweather(request):
	if request.method=="POST":
		try:
			city=request.POST.get('city')
			a1="http://api.openweathermap.org/data/2.5/weather?units=metric"
			a2="&q="+city
			a3="&appid="+"c6e315d09197cec231495138183954bd"
			wa=a1+a2+a3
			res=requests.get(wa)
			data=res.json()
			temp=data['main']['temp']
			desc=data['weather'][0]['description']
			icon="http://api.openweathermap.org/img/w/"+data['weather'][0]['icon']+".png"
			msg="Temperature="+str(temp)+" description="+str(desc)
			return render(request, 'checkweather.html', {'msg':msg, 'icon':icon})
		except Exception as e:
			return render(request, 'checkweather.html', {'msg':'city not found'})
	
	else:
		return render(request, 'checkweather.html')

def showtodo(request):
	data=TodoModel.objects.filter(user=request.user)
	return render(request, 'showtodo.html', {'data':data})
def addtodo(request):
	if request.user.is_authenticated:
		user=request.user
		if request.method=="POST":
			f=TodoForm(request.POST)
			if f.is_valid():
				f.save()
				fm=TodoForm()
				return render(request, 'addtodo.html', {'fm':fm, 'msg':'Task added :)'})
			else:
				fm=TodoForm()
				return render(request, 'addtodo.html', {'fm':f, 'msg':'Check for Errors!!!'})
		else:
			fm=TodoForm(initial={'user':request.user})
			return render(request, 'addtodo.html', {'fm':fm})
def deletetask(request, id):
	d=TodoModel.objects.get(uid=id)
	d.delete()
	return redirect('showtodo')
def search(request):
	s=request.GET.get('search')
	data=TodoModel.objects.filter(task=s)
	return render(request, 'showtodo.html', {'data':data})
	