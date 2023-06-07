from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class CreatingUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                                'class': 'sign__input',
                                                                }))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email',
                                                                'class': 'sign__input',
                                                                }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                'class': 'sign__input',
                                                                }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                'class': 'sign__input',
                                                                }))
    


class LoginForm(AuthenticationForm):

     username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                                'class': 'sign__input',
                                                                }))
     password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                'class': 'sign__input',
                                                                }))