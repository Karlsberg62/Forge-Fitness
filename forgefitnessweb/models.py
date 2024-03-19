from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    #Name, Age, Gender, Phone, Email, Address, Current Plan 
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    gender_choice = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choice)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    postcode = models.TextField(default="")
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user}' 
 
class Sessions(models.Model):
    title = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=200)
    time = models.TimeField()
    date = models.DateField()
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it's not already set
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} class at {self.location}, {self.time}"   
    
class CommentReview(models.Model):

    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')
    post = models.ForeignKey(Sessions, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.created_on}" 
