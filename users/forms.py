from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import CustomUser

class UserSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Write your name..'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Write your last name..'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Write your username..'}))
    password1 = forms.CharField(required=True, label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(required=True, label="Confirm Password", widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))


    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','username','password1','password2']

class UserSignInForm(AuthenticationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Write your username..'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Write your password..'}))

class UserUpdateForm(UserChangeForm):
    first_name = forms.CharField(required=True)
    username = forms.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'profile_image', 'bio']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Write your name..'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Write your last name..'}),
            'username': forms.TextInput(attrs={'placeholder': 'Write your username..'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Write your email..'}),
            'bio': forms.Textarea(attrs={'placeholder': 'Write your bio..'}),
        }