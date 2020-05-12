from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from shop.models import Shop
from .models import User



class ShopSerializer(serializers.ModelSerializer):
	
	class Meta:
		
		model = Shop
		fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):

	shop = ShopSerializer(many=False, read_only=True)
	shop_id = serializers.IntegerField(write_only=True)
	
	class Meta:
		
		model = User
		fields = ['id', 'username', 'first_name', 'last_name', 'shop', 'shop_id']
		
