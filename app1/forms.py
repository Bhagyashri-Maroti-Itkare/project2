from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# for adding surname and email in registeration form / new column add hot aahe

class singupform1(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

from django.contrib.auth.forms import UserChangeForm

class edit_user_profile_form(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

