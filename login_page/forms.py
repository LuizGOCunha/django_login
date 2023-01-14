from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=200, required=True)
    # Here the PasswordInput is used as widget to hide the input values
    password = forms.CharField(max_length=20, widget=forms.PasswordInput, required=True)
    password_c = forms.CharField(max_length=20, widget=forms.PasswordInput, required=True, label="Confirm your Password")

class SigninForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(max_length=20,widget=forms.PasswordInput, required=True)