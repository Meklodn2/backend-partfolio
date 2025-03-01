from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, DetailView, UpdateView
from .models import CustomUser
from .forms import UserSignUpForm, UserSignInForm, UserUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
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
    return redirect('login')

class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'main/profile.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        return self.request.user