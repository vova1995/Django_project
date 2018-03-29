from django.db import models

# Create your models here.
class UserProfile(models.Model):
	name = models.CharField(max_length=150, default='')
	surname = models.CharField(max_length=150, default='')
	email = models.EmailField()
