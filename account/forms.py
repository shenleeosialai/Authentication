from django import forms
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username eg. john doe'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password eg 123@wrf'}))


class UserRegistrationForm(forms.MOdelForm):
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput
    )
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'email')