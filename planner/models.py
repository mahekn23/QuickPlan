from django.db import models
from django.db.models import Model
from django.conf import settings 
from django.contrib.auth.models import User
import datetime
import requests

# Create your models here.
class TodoModel(models.Model): 
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	uid=models.AutoField(primary_key=True)
	task=models.CharField(max_length=500)
	deadline=models.CharField(max_length=50, default='Null')
	note=models.CharField(max_length=150, default='Null')
	time=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.task
