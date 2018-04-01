from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'password',)
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Имя пользователя'}),
        }

'''class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)

class EditProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        profile = kwargs.get('instance')
        if profile:
            kwargs['instance'] = profile.user

        self.user_form = EditUserForm(*args, **kwargs)

        self.fields.update(self.user_form.fields)
        self.initial.update(self.user_form.initial)

    def save(self, *args, **kwargs):
        self.user_form.save(*args, **kwargs)
        return super(EditProfileForm, self).save(*args, **kwargs)

    class Meta:
        model = User
        exclude = ('user',)'''