from django import forms
from .models import CustomUser, LinkUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'url', 'avatar']
        # fields = ['username', 'email', 'bio', 'url']

class LoginCustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']

class LinksForm(forms.ModelForm):
    class Meta:
        model = LinkUser
        fields = ['link', 'url']
