from django.shortcuts import render
from .forms import SignupForm

# Create your views here.

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        # Get your values and clean the post request here
        pass

    context = {}
    context['form'] = SignupForm
    return render(request, 'signup.html', context)

def home(request):
    return render(request, 'home.html')

def signout(request):
    pass

