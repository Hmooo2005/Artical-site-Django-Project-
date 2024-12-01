from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Artical(models.Model):
	x = (
		('programming', 'programming'),
		('medicine', 'medicine'), 
		('computer', 'computer'),
		('phones', 'phones'),
		('cooking', 'cooking'),
	)

	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=20)
	content = models.TextField()
	img = models.ImageField(upload_to='artical_pic')
	artical_date = models.DateTimeField(auto_now_add=True)
	category = models.CharField(max_length=30, choices=x, default="cooking")
	
	def __str__(self):
		return self.title

	def get_absolute_url(self): # need to right the name of the method correctly
		return reverse('artical_details', kwargs={'pk':self.pk})
	



class Comment(models.Model):
	post = models.ForeignKey(Artical, related_name='comments', on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField()

	def get_absolute_url(self): # need to right the name of the method correctly
		return reverse('artical_details', kwargs={'pk':self.pk})
