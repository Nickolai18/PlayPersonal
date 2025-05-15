from django import forms
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.models import User

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