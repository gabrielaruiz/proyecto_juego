from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.db import connection

# Create your models here.
class usuario(models.Model):
	Nick=models.CharField(max_length=100)
	Email=models.EmailField(max_length=100)
	Password=models.CharField(max_length=20)

	def __unicode__(self):
		return "%s "%(self.Nick)
