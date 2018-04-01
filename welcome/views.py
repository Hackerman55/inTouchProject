from .models import Profile
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from welcome.forms import SignUpForm, EditProfileForm
from django.contrib import auth
from django.contrib.auth.forms import UserChangeForm
#from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse



# Create your views here.
def home(request):
    username = auth.get_user(request)
    context = {"username": username}
    return render(request, 'welcome/start.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('')
    else:
        form = SignUpForm()
    return render(request, 'welcome/signup.html', {'form': form})

def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/profile/')

    else:
        form = EditProfileForm(instance=request.user)
        context = {'form':form}
        return render(request,  'welcome/edit_profile.html', context)