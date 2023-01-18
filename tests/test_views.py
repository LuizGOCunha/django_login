from django.test import Client
from django.urls import reverse

from login_page.views import signin, signup, signout, home

def test_signin_view_status_code():
    client = Client()
    response = client.get(reverse("signin"))
    assert response.status_code == 200
    print(type(response.templates))


def test_signup_view_status_code():
    client = Client()
    response = client.get(reverse("signup"))
    assert response.status_code == 200

def test_signout_view_status_code():
    client = Client()
    response = client.get(reverse("signout"))
    # Status is 302 due to returning a redirect
    assert response.status_code == 302

def test_home_view_status_code():
    client = Client()
    response = client.get(reverse("home"))
    assert response.status_code == 200