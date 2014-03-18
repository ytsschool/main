from django.db import models
from django.forms import ModelForm
# Create your models here.
class board(models.Model):
        title = models.CharField(max_length=128, null=False)
	description = models.CharField(max_length=400,null=False)
	money = models.FloatField(default=0.0)
	contact = models.CharField(max_length=128, null=False)
        pub_date = models.DateTimeField('date published', auto_now_add=True)
	def __str__(self):
        	return self.title
	def get_absolute_url(self):
        	return "/board/%i/" % self.id
