
from django.contrib import admin
from django.urls import path, include
from . import views

# Remember to import views

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('', views.home, name='home')
]