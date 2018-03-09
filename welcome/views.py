from django.shortcuts import render
from .models import Profile


# Create your views here.
def index(request):
    profiles = Profile.objects.all()
    return render(request, 'welcome/start.html', {'profiles': profiles})


