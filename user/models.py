from django.db import models
from django.contrib.auth.models import AbstractUser

from shop.models import Shop


class UserType(models.Model):

	user_type = models.CharField(max_length = 200, unique = True)

	def __str__(self):
	
		return  self.user_type


class User(AbstractUser):

	user_type = models.ForeignKey(UserType, on_delete = models.SET_NULL, blank = True, null = True)
	shop = models.ForeignKey(Shop, on_delete = models.SET_NULL, blank = True, null = True, related_name = 'users')
	
	def __str__(self):
	
		return self.username
