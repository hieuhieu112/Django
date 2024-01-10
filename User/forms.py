from django import forms
from .models import User
from Group.models import Group
from Message.models import Message


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ("creator", "name", "status")


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('sender',  "type", "message")


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("images", "password", "email", "phone", "status", "first_name", "last_name", "username")
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First name', 'required': 'required'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name', 'required': 'required'}),
            'email': forms.TextInput(attrs={'placeholder': 'Enter your email',
                                            'required': 'required', 'type': 'email'}),
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username', 'required': 'required'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter your number', 'required': 'required'}),
            'password': forms.TextInput(attrs={'placeholder': 'Enter your password',
                                               'required': 'required', 'type': 'password'}),
            'images': forms.FileInput(attrs={}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your username', 'name': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'from', 'type': 'password',
                                                                 'placeholder': 'Enter your password',
                                                                 'name': 'password'}))
