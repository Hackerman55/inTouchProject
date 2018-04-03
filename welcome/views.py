#from .models import Profile
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect #get_object_or_404
from welcome.forms import SignUpForm, UserForm, ProfileForm, MessengersForm #EditProfileForm,
from django.contrib import auth
#from django.contrib.auth.forms import UserChangeForm
#from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.db import transaction


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
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'welcome/signup.html', {'form': form})

'''def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/profile/')

    else:
        form = EditProfileForm(instance=request.user)
        context = {'form':form}
        return render(request,  'welcome/edit_profile.html', context)'''
@login_required
@transaction.atomic
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        mssg_form = MessengersForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/profile/')
        elif mssg_form.is_valid():
            mssg_form.save()
            #messages.success(request, _('Your profile was successfully updated!'))
            return redirect('/profile/')
        #else:
            #messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        mssg_form = MessengersForm(instance=request.user.profile)
    return render(request, 'welcome/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'mssg_form': mssg_form,
    })
