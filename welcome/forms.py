from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile
from awesome_avatar import forms as avatar_forms

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердить пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Имя пользователя'}),
        }


'''class EditProfileForm(UserChangeForm):

    class Meta:
        model = Profile
        fields = ('username')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Имя пользователя'}),
        }'''

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
class AvatarChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar',)

class UploadAndCropImageForm(forms.Form):
    image = avatar_forms.AvatarField()



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