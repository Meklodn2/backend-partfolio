from django.urls import path
from users.views import SignUpView, SignInView, user_logout
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', SignInView.as_view(), name='login'),
    path('', user_logout, name='logout'),
]
