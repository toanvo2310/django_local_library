from django import forms
from django.contrib.auth.models import User
import re

class RegistrationForm(forms.Form):

    username   = forms.CharField(label = 'Username', max_length = 30)
    email      = forms.EmailField(label = 'Email')
    password_1 = forms.CharField(label = 'Password', widget = forms.PasswordInput())
    password_2 = forms.CharField(label = 'Password again', widget = forms.PasswordInput())

    def clean_password_2(self):

        if 'password_1' in self.cleaned_data:
            password_1 = self.cleaned_data['password_1']
            password_2 = self.cleaned_data['password_2']

            if password_1 == password_2:
                return password_2

        raise forms.ValidationError('Invalid password')

    def clean_username(self):

        username = self.cleaned_data['username']

        if not re.search(r'^[\w]+$', username):
            raise forms.ValidationError('Invalid username')

        try:
            User.objects.get(username = username)
        except User.DoesNotExist:
            return username

        raise forms.ValidationError('Username already exists')

    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password_1'])
        