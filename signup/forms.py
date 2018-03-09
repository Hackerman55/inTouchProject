from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.models import User


class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs = {'placehold':'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs = {'placehold':'Enter Password'}))
    class Meta:
       model = User
       fields = ('email',)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Пароли не совпадают!")

        return password2
