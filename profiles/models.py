from django.db import models

# Create your models here.

class UserProfile(models.Model):
    image = models.FileField(upload_to='images') # this file should be stored on hard drive, not cloud storage, only the path should be stored in database; upload_to to work, need to add MEDIA_ROOT in main project settings.py