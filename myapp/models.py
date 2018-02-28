from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
 model=models.CharField(max_length=20)
 detail=models.CharField(max_length=100)
 price=models.DecimalField(max_digits=20,decimal_places=2)

class Rent(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	car=models.ForeignKey(Car, on_delete=models.CASCADE)
	start=models.DateTimeField()
	stop=models.DateTimeField()
	fee=models.DecimalField(max_digits=20,decimal_places=2)

class Person(models.Model):
	name=models.CharField(max_length=100)
	dob=models.DateField(blank=True,null=True)
	def __unicode__(self):
		return u"%s"%(self.name)

class Image(models.Model):
	image=models.ImageField(upload_to='images')
	description=models.CharField(max_length=100,blank=True,null=True)

class Return(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	car=models.ForeignKey(Car, on_delete=models.CASCADE)
	stop=models.DateTimeField()