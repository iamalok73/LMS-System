from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    mobile = forms.CharField(max_length=15)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'mobile', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label="Email or Mobile")


class ForgetPasswordForm(forms.Form):
    email = forms.EmailField()
