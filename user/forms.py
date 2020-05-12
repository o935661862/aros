from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User



class SignupForm(UserCreationForm):
    
	email = forms.EmailField(max_length=200, help_text='Required')
	
	
	class Meta:
	
		model = User
		fields = ('username', 'email', 'password1', 'password2')
		
		

class UserForm (forms.ModelForm):

		
	class Meta:
	
		model = User
		fields = ('last_name','first_name','user_type',)

