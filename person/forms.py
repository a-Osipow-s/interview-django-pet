
from django import forms
from django.conf import settings

class UserLoginForm(forms.ModelForm):

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
        }