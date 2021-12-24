from django.db import models

# Create your models here.
class EmailLists(models.Model):
	email 		 = models.EmailField(verbose_name="email", max_length=100)
	date         = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.email