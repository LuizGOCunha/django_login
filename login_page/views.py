from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import SignupForm

# Create your views here.

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    context = {}
    context['form'] = SignupForm

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_c = request.POST['password_c']
        if password == password_c:
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email, 
                password=password
            )
            # redirect to another page (home, but logged in)
            print("*************************", user)
            context["message"] = "User created successfully!"
        else:
            context["message"] = "Your passwords do not match"
            print("--------------------------------")
        # Get your values and clean the post request here
        pass

    return render(request, 'signup.html', context)

def home(request):
    return render(request, 'home.html')

def signout(request):
    pass

