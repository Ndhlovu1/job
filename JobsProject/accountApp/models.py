from django.db import models
from django.conf import settings

class Profile(models.Model):
    #1to1 Field allows us to associate profiles with Users
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    date_of_birth = models.DateField(blank=True, null=True)
    field_of_study = models.CharField(max_length=250, null=True, blank=True)

    institution = models.CharField(max_length=250, null=True, blank=True)
    bio =  models.TextField(max_length=500,null=True, blank=True)
    profile_photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    last_job = models.CharField(max_length=255,null=True, blank=True)
    company = models.CharField(max_length=255,null=True, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
   
    def __str__(self):
        return f"{self.user.first_name}'s Profile" 

 
