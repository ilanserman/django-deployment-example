from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    #use User class from django
    user = models.OneToOneField(User,on_delete=models.CASCADE) #with this we add aditional fields that User doesn't have

    #additional classes

    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True) #requires pillow to be installed

    def __str__(self):
        return self.user.username #username is the default attribute for class User
