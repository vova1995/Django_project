from django.db import models

class Catalog(models.Model):
	name = models.CharField(max_length=150)
	place = models.CharField(max_length=150)
	price = models.IntegerField(default=0)
	
	def __str__(self):
		return self.name + '  ' + self.place + '  ' + str(self.price)