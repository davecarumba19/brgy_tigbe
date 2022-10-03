from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profiles, Reports, Requests


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'Enter Username', 'class':'registerInput'})
        self.fields['first_name'].widget.attrs.update({'placeholder':'Enter First Name', 'class':'registerInput'})
        self.fields['last_name'].widget.attrs.update({'placeholder':'Enter Last Name', 'class':'registerInput'})
        self.fields['email'].widget.attrs.update({'placeholder':'Enter Email', 'class':'registerInput'})
        self.fields['password1'].widget.attrs.update({'placeholder':'Enter Password', 'class':'registerInput'})
        self.fields['password2'].widget.attrs.update({'placeholder':'Confirm Password', 'class':'registerInput'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profiles
        fields = ['email','address','status', 'gender']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder':'Edit Email', 'class':'editUpdateAccountInput'})
        self.fields['address'].widget.attrs.update({'placeholder':'Edit Address', 'class':'editUpdateAccountInput'})
        self.fields['status'].widget.attrs.update({'placeholder':'Edit Status', 'class':'editUpdateAccountInput'})
        self.fields['gender'].widget.attrs.update({'placeholder':'Edit Gender', 'class':'editUpdateAccountInput'})


class ReportsForm(ModelForm):
    class Meta:
        model = Reports
        fields = ['location', 'message']
