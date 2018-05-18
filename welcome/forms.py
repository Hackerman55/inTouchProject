from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердить пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Имя пользователя'}),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Имя пользователя'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('description',)
        widgets = {
            'description': forms.TextInput(attrs={'placeholder': 'Описание'}),
        }

class MessengersForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('vk', 'telegram', 'whatsapp', 'viber', 'skype', 'insta',)
        widgets = {
            'vk': forms.TextInput(attrs={'placeholder': 'username'}),
            'telegram': forms.TextInput(attrs={'placeholder': 'username or phone number'}),
            'whatsapp': forms.TextInput(attrs={'placeholder': 'phone number'}),
            'viber': forms.TextInput(attrs={'placeholder': 'phone number'}),
            'skype': forms.TextInput(attrs={'placeholder': 'username'}),
            'insta': forms.TextInput(attrs={'placeholder': 'username'}),
        }

