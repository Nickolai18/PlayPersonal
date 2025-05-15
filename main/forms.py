from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

from django.contrib.auth.models import User

from main.models import Games



class AddGames(forms.ModelForm):

  name = forms.CharField()
  description = forms.CharField()
  image = forms.ImageField(required=False)
  link = forms.CharField(required=False)
  class Meta:
    model = Games
    fields = {
      "name",
      "description",
      "image",
      "link",
    }
    

class UserLoginForm(AuthenticationForm):

  username = forms.CharField(
    widget=forms.TextInput(attrs={
      'autofocus': True,
      'class': 'form-control',
      'aria-describedby': 'emailHelp',
      'id': 'exampleInputEmail1'
    }))
  password = forms.CharField(
    widget=forms.TextInput(attrs={
      'class': 'form-control',
      'type': 'password',
      'id': 'exampleInputPassword1'
    }))

  class Meta:
    model = User

class UserRegistrationForm(UserCreationForm):

  class Meta:
    model = User
    fields = {
      "username",
      "password1",
      "password2",
    }
  username = forms.CharField()
  password1 = forms.CharField()
  password2 = forms.CharField()
  