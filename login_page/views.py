from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import SignupForm, SigninForm

# Create your views here.

def signin(request):
    context = {}
    context['form'] = SigninForm
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            context['autenticated'] = request.user
            return redirect('/')
        else:
            context['message'] = "Invalid Credentials"
        
    return render(request, 'signin.html', context)

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
            context["message"] = "User created successfully!"
            return redirect("/signin/")
        else:
            context["message"] = "Your passwords do not match"
        # Get your values and clean the post request here
        pass

    return render(request, 'signup.html', context)

def home(request):
    context = {}
    if request.user.is_authenticated:
        context['autenticated'] = request.user

    return render(request, 'home.html', context)

def signout(request):
    logout(request)
    return redirect('/')

