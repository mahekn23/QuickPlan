from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from random import randrange
from django_project.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
# Create your views here.
def usignup(request):
	if request.method=="POST":
		un=request.POST.get('un')
		em=request.POST.get('em')
		try:
			usr=User.objects.get(username=un)
			return render(request, 'usignup.html', {'msg':'Username already exists!!'})
		except User.DoesNotExist:
			try:
				usr=User.objects.get(email=em)
				return render(request, 'usignup.html', {'msg':'Email already exists!!'})
			except User.DoesNotExist:
				pw=""
				text="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRTSUVWXYZ"
				for i in range(8):
					pw=pw+text[randrange(len(text))]
				print(pw)
				subject="Welcome to our website"
				msg="ur password is "+str(pw)
				send_mail(subject, msg, EMAIL_HOST_USER, [em])
				usr=User.objects.create_user(username=un, password=pw, email=em)
				usr.save()
				return redirect('ulogin')
	else:
		return render(request, 'usignup.html')
def fp(request):
	if request.method=="POST":
		un=request.POST.get('un')
		em=request.POST.get('em')
		usr=User.objects.get(username=un)
		pw=""
		text="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRTSUVWXYZ"
		for i in range(8):
			pw=pw+text[randrange(len(text))]
		print(pw)
		subject="Your New Password"
		msg="ur password is "+str(pw)
		send_mail(subject, msg, EMAIL_HOST_USER, [em])
		usr.set_password(pw)
		usr.save()
		return redirect('ulogin')
	else:
		return render(request, 'fp.html')
def ulogin(request):
	if request.method=="POST":
		un=request.POST.get('un')
		pw=request.POST.get('pw')
		usr=authenticate(username=un, password=pw)
		if usr is None:
			return render(request, 'ulogin.html', {'msg':'Invalid credentials!!'})
		else:
			login(request, usr)
			return redirect('home')
	else:
		return render(request, 'ulogin.html')
def ulogout(request):
	logout(request)
	return redirect('ulogin')

def index(request):
	return render(request, 'index.html')

					