from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

def validate_email(value):
    if User.objects.filter(email = value).exists():
        raise ValidationError((f"{value} is taken."),params = {'value':value})

class UserRegistrationForm(UserCreationForm):
        email =  forms.EmailField(required=True,validators = [validate_email])
        
        class Meta:
            model = User
            # model._meta.get_field('email')._unique = True
            fields = ['username', 'email', 'password1', 'password2'] 