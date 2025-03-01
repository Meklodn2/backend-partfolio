from django.urls import path
from users.views import SignUpView, SignInView, user_logout, ProfileView
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', ProfileView.as_view(),name='profile'),
]
