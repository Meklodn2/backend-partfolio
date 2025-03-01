from django.contrib.auth import login, logout
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from .models import CustomUser
from .forms import UserSignUpForm, UserSignInForm, UserUpdateForm
from django.urls import reverse_lazy

# Create your views here.

class SignUpView(CreateView):
    model = CustomUser
    form_class = UserSignUpForm
    template_name = 'main/auth/sign_up.html'
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        user = form.save()
        login (self.request, user)
        return super().form_valid(form)

class SignInView(LoginView):
    form_class = UserSignInForm
    template_name = 'main/auth/sign_in.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

def user_logout(request):
    logout(request)
    return render(request,'main/auth/sign_in.html')