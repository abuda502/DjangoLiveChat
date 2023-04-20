from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, validate_email

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, validators=[validate_email])
    username = forms.CharField(max_length=30, required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(), validators=[MinLengthValidator(8)])
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')


        