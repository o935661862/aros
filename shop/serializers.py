from rest_framework import serializers

from user.models import User
from .models import Shop



class OwnerSerializer(serializers.ModelSerializer):
	
	class Meta:
		
		model = User
		fields = ['id', 'username']


class ShopSerializer(serializers.ModelSerializer):

	owner = OwnerSerializer(many=False, read_only=True)
	owner_id = serializers.IntegerField(write_only=True)
	
	class Meta:
		
		model = Shop
		fields = ['id', 'name', 'owner', 'owner_id']