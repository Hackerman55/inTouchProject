from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердить пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Имя пользователя'}),
        }
