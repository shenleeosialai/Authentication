from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username eg. john doe'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password eg 123@wrf'}))