from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    #Name, Age, Gender, Phone, Email, Address, Current Plan 
    user = models.OneToOneField(User, on_delete=models.CASCADE) #Delete profile when user is deleted
    name = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
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

class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

class Classes(models.Model):
    title = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=200)
    time = models.TimeField()
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it's not already set
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} class at {self.location}, {self.time}"   
    
