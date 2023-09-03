from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from authuser.models import User
from .models import Post
from django.utils.translation import gettext,gettext_lazy 

class SignUpForm(UserCreationForm):
	password1=forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'forms-control'}))
	password2=forms.CharField(label='confirm password(again)',widget=forms.PasswordInput(attrs={'class':'forms-control'}))
    
	class Meta:
		model = User
		fields = ['email','name']
		label={'name':'Name','email':'Email'}
		widget={'email':forms.TextInput(attrs={'class':'forms-control'}),
		'name':forms.EmailInput(attrs={'class':'forms-control'})
		}

class loginForm(AuthenticationForm):
	username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'forms-control'}))
	password=forms.CharField(label=("password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'forms-control'}))	

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','desc',]
        label={'title':forms.TextInput(attrs={'class':'forms-control'}),
        'desc':forms.TextInput(attrs={'class':'forms-control'}),}

class PostForm_status(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','desc','status']
        label={'title':forms.TextInput(attrs={'class':'forms-control'}),
        'desc':forms.TextInput(attrs={'class':'forms-control'}),
        'status':forms.ChoiceField()}        


        
                	


