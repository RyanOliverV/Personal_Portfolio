from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#These are ready made classes to create common forms and authenication systems
#Found in Django documentation here: https://docs.djangoproject.com/en/4.1/topics/auth/default/
class UserRegistration(UserCreationForm):
    email = forms.EmailField()

    #Meta class provides a nested namespace for configurations, and keeps them all in one place
    class Meta:
        model = User #defines what model this form interacts with
        #defines what fields that are shown on the form
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    #Meta class provides a nested namespace for configurations, and keeps them all in one place
    class Meta:
        model = User #defines what model this form interacts with
        #defines what fields are shown on the form
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):

    #Meta class provides a nested namespace for configurations, and keeps them all in one place
    class Meta:
        model = Profile #defines what model this form interacts with
        #defines what fields are shown on the form
        fields = ['image']