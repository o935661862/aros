from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


from .models import User
from .forms import SignupForm, UserForm
from .serializers import UserSerializer
from .permissions import AdminPermission, IsSelfOrAdmin
from .tokens import account_activation_token
# @/./+/-/_only.


def signup(request):

	if request.method == 'POST':
	
		form = SignupForm(request.POST)
		print(request.POST)
		print(form)
		print(form.errors)
		
		if form.is_valid():
		
			user = form.save(commit=False)
			user.is_active = False
			user.save()
			current_site = get_current_site(request)
			mail_subject = 'Activate your aros account.'
			message = render_to_string('user/account_activation_email.html', {
				'user': user,
				'domain': current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)),
				'token': account_activation_token.make_token(user),
			})
			to_email = form.cleaned_data.get('email')
			email = EmailMessage(mail_subject, message, to=[to_email])
			email.send()
			
			return HttpResponse('Please confirm your email address to complete the registration')
	else:
	
		form = SignupForm()
		
	return render(request, 'user/signup.html', {'form': form})
		
	
	
def activate(request, uidb64, token):

	try:
	
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
		
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
	
		user = None
		
	if user is not None and account_activation_token.check_token(user, token):
	
		user.is_active = True
		user.save()
		login(request, user)
		
		return  render(request, 'user/confirmation_successefull.html')
	
	else:
	
		return HttpResponse('Activation link is invalid!')

	

class LoginView(LoginView):

	template_name = 'user/login.html'


	def get_success_url(self):
		
		return reverse('user:user')
		# return reverse('user:user', kwargs={'pk':self.request.user.id})

def index(request, exception = None):
    return render(request, template_name='index.html')


class CustomAuthToken(ObtainAuthToken):

	def post(self, request, *args, **kwargs):
		
		serializer = self.serializer_class(data=request.data, context={'request': request})
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		token, created = Token.objects.get_or_create(user=user)
		
		return Response({
			'token': token.key,
			'id': user.id,
			'username': user.username,
			'first_name': user.first_name,
			'last_name': user.last_name,
			'user_type': user.user_type_id,
		})
		


class CustomAuthTokenRemover(APIView):

	def post(self, request, format = None):
		
		request.user.auth_token.delete()
		
		return Response(status = status.HTTP_200_OK)



class UserViewSet(viewsets.ModelViewSet):
	
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [IsSelfOrAdmin]



class ListUsers(APIView):

	permission_classes = [AdminPermission]
	
	def get(self, request, format = None):
		
		user_values = User.objects.all().values('id', 'username')
		
		return Response(user_values)
		