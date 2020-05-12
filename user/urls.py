from django.urls import path, re_path, include
from django.views.generic import TemplateView

from rest_framework import routers

from . import views
from .views import LoginView, UserViewSet, ListUsers


router = routers.DefaultRouter()
router.register('user', UserViewSet)

urlpatterns = [
	
	path('signup', views.signup, name='signup'),
	re_path(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
	path('login/', LoginView.as_view(), name='login'),
	
	
	# path('api/list_users', ListUsers.as_view(), name='list_users'),
	# path('api/', include(router.urls)),
]