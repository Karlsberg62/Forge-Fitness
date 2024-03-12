from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    #Name, Age, Gender, Phone, Email, Address, Current Plan 
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender_choice = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choice)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    
    def __str__(self):
        return self.name