from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework.authtoken import views

from user.views import index
from user.views import CustomAuthToken, CustomAuthTokenRemover, UserViewSet, ListUsers
from shop.views import ShopViewSet, ListShops

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('shop', ShopViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
	path('', index, name='index'),
	path('user/', include(('user.urls', 'user'), namespace = 'user')),
	path('shop/', include(('shop.urls','shop'), namespace = 'shop')),
	path('api/get_token', CustomAuthToken.as_view()),
	path('api/delete_token', CustomAuthTokenRemover.as_view()),
	path('api/list_users', ListUsers.as_view(), name='list_users'),
	path('api/list_shops', ListShops.as_view(), name='list_shops'),
	path('api/', include(router.urls)),
]