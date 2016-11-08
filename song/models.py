from django.db import models
from django.contrib.auth.models import User

class Songs(models.Model):
	Artist=models.CharField(max_length=500)
	name=models.CharField(max_length=500)
	genre=models.CharField(max_length=500)
	album=models.CharField(max_length=500)
	link=models.CharField(max_length=500)
	abuse=models.IntegerField(blank=True)
	
class playlist(models.Model):
	song=models.ForeignKey(Songs,unique=False,blank=True)
	user=models.ForeignKey(User,unique=False)

class Comments(models.Model):
	song=models.ForeignKey(Songs,unique=False,blank=True)
	user=models.ForeignKey(User,unique=False)
	comment=models.CharField(max_length=999999)
class Feedback(models.Model):
	feedback=models.CharField(max_length=10000)
	song = models.ForeignKey(Songs, unique=False, blank=True)
	user = models.ForeignKey(User, unique=False)

