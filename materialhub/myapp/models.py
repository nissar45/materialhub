from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Materials(models.Model):
    name=models.CharField(max_length=200)
    type=models.CharField(max_length=200)
    about=models.CharField(max_length=200)
    photo=models.CharField(max_length=200)
    amount=models.FloatField()

class Stock(models.Model):
    stock_no=models.IntegerField()
    date=models.DateField()
    MATERIAL=models.ForeignKey(Materials,on_delete=models.CASCADE)


class Driver(models.Model):
    name=models.CharField(max_length=200)
    photo=models.CharField(max_length=200)
    proof=models.CharField(max_length=200)
    place=models.CharField(max_length=200)
    pin=models.CharField(max_length=200)
    post=models.CharField(max_length=200)
    number=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    AUTHUSER=models.OneToOneField(User,on_delete=models.CASCADE)


class Users(models.Model):
    name=models.CharField(max_length=200)
    photo=models.CharField(max_length=400)
    place=models.CharField(max_length=200)
    pin=models.CharField(max_length=200)
    post=models.CharField(max_length=200)
    number=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    AUTHUSER=models.OneToOneField(User,on_delete=models.CASCADE)

class User_request(models.Model):
    date=models.DateField()
    status=models.CharField(max_length=200)
    MATERIAL=models.ForeignKey(Materials,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    USERS=models.ForeignKey(Users,on_delete=models.CASCADE)

class Allocation(models.Model):
    DRIVER=models.ForeignKey(Driver,on_delete=models.CASCADE)
    REQUEST=models.ForeignKey(User_request,on_delete=models.CASCADE)
    date=models.DateField()
    status=models.CharField(max_length=200)

class Feedback(models.Model):
    date=models.DateField()
    feedback=models.CharField(max_length=200)
    rating=models.CharField(max_length=200)
    USERS=models.ForeignKey(Users,on_delete=models.CASCADE)

class Payment(models.Model):
    date=models.DateField()
    status=models.CharField(max_length=200)
    USERS=models.ForeignKey(Users,on_delete=models.CASCADE)
    amount=models.FloatField()
    ALLOCATION=models.ForeignKey(Allocation,on_delete=models.CASCADE)

class Complaint(models.Model):
    date=models.DateField()
    complaint=models.CharField(max_length=200)
    USERS=models.ForeignKey(Users,on_delete=models.CASCADE)
    reply=models.CharField(max_length=200)

    status=models.CharField(max_length=200)

class Location(models.Model):
    AUTHUSER=models.OneToOneField(User,on_delete=models.CASCADE)
    latitude=models.CharField(max_length=200)
    longitude=models.CharField(max_length=200)
