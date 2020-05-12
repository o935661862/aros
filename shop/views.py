from django.db.models import F

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response

from user.permissions import AdminPermission

from .serializers import ShopSerializer
from .models import Shop



class ListShops(APIView):

	def get(self, request, format = None):	
        
		shop_values = Shop.objects.all().values('id', 'name')
		
		return Response(shop_values)



class ShopViewSet(viewsets.ModelViewSet):
	
	queryset = Shop.objects.all().annotate(owner_string = F('owner__last_name'))
	serializer_class = ShopSerializer
	permission_classes = [AdminPermission]
		
