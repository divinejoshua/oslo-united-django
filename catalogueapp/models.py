from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
import random

def upload_location(instance, filename):
	file_path = 'oslounitedcompany/{image}'.format(image=filename)
	return file_path


# Create your models here.
class Catelogues(models.Model):
	title        = models.CharField(max_length=100)
	slug         = models.SlugField(unique=True, blank=True)
	body         = models.TextField()
	date         = models.DateTimeField(auto_now_add=True)
	thumb        = models.ImageField(blank=True, upload_to=upload_location)
	# author       = models.ForeignKey(User, default=None,  on_delete=models.CASCADE)
	
	def __str__(self):
		return self.title
			
def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title+str(random.randint(0,22)))

pre_save.connect(pre_save_blog_post_receiver, sender=Catelogues)




# Create your models here.
class Products(models.Model):
	title        = models.CharField(max_length=100)
	price        = models.PositiveIntegerField(blank=True)
	body         = models.TextField()
	date         = models.DateTimeField(auto_now_add=True)
	catelogue 	 = models.ForeignKey(Catelogues, default=None, on_delete=models.CASCADE)
	thumb        = models.ImageField(blank=True, upload_to=upload_location)
	# author       = models.ForeignKey(User, default=None,  on_delete=models.CASCADE)

	def __str__(self):
		return self.title
			