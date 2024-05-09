from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser





class MissingCase(models.Model):
   name = models.CharField(max_length=30)
   age = models.PositiveIntegerField()
   description = models.TextField()
   identificationMark = models.CharField(max_length=3)
   height = models.PositiveIntegerField()
   weight = models.PositiveIntegerField()
   GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
   gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
   number = models.PositiveIntegerField()
   image = models.ImageField(upload_to='images/', null=True, blank=True)
  
   def __str__(self):
       return self.name
   

class CrimeReport(models.Model):
    case_id = models.PositiveIntegerField()
    crime_no = models.PositiveIntegerField()
    crime_type = models.TextField(max_length=20)
    crime_name = models.TextField(max_length=35)
    age = models.PositiveIntegerField()
    nickname = models.TextField(max_length=15)
    adate = models.DateField()
    dateoc = models.DateField()
    gender = models.TextField()
    address = models.CharField(max_length=60)
    birthmark = models.TextField(max_length=5)
    wanted = models.TextField()
    pending = models.TextField()
    def __str__(self):
       return self.crime_name

from django.db import models

class UserA(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class ContactSubmission(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name