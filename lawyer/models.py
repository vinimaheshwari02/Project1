from django.db import models
class Cost(models.Model):
	name=models.CharField(max_length=200)
	
	address=models.CharField(max_length=200)
	about=models.CharField(max_length=200)
# Create your models here.
