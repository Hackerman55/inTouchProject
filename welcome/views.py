from .models import Profile
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from welcome.forms import SignUpForm

# Create your views here.
def index(request):
    profiles = Profile.objects.all()
    return render(request, 'welcome/start.html', {'profiles': profiles})


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
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'welcome/signup.html', {'form': form})
