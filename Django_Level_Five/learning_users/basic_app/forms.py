from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
#because we want to modify this attribute, but it's built in already

    class Meta():
        model = User #must always be named model
        fields = ('username','email','password') #always named fields

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo  #always named model
        fields = ('portfolio_site','profile_pic') #always named fields
