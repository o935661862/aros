from django.urls import path
from .views import ListShops

urlpatterns = [
	path('api/list_shops', ListShops.as_view(), name='list_shops'),
]