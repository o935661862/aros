from django.db import models
from django.conf import settings


class Shop (models.Model):

	created_at  =  models.DateTimeField(auto_now_add = True)
	updated_at  =  models.DateTimeField(auto_now = True,)
	created_by  =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, related_name = 'shop_created_by', blank = True, null = True)
	updated_by  =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, related_name = 'shop_updated_by', blank = True, null = True)
	
	name = models.CharField(max_length = 200, unique = True)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = 'owner', blank = True, null = True)
	
	def __str__(self):
	
		return  self.name