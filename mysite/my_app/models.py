from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class UserProfile(models.Model):#we created UserProfile in order to show it in admin and then we used it in profile page
	user = models.OneToOneField(User)
	name = models.CharField(max_length=150, default='')
	surname = models.CharField(max_length=150, default='')
	email = models.EmailField()

	def __str__(self):
		return 'User: ' + str(self.user) + ', ' + 'Surname:  '+ self.surname + ', ' + 'Email: ' + self.email
		# return str(self.user) + '\t' + self.surname + '\t' + self.email

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)