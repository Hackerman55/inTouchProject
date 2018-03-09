from django.shortcuts import render, redirect
from signup.forms import RegisterUserForm
from django.contrib import auth
from django.views.generic import CreateView
from django.http import HttpResponse, HttpResponseForbidden


# Create your views here.
def index(request):
    return render(request, 'login/signup.html')

def signup(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST or None)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.set_password(form.cleaned_data['password'])
            profile.save()
            return redirect('postlist')
    else:
        form = RegisterUserForm()
    context = {
        'form':form,
        }
    return render(request, 'login/signup.html', context)

