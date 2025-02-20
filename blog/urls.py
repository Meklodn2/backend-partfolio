from django.urls import path    
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='blog'),
    path('<int:pk>/', PostDetailView.as_view(), name='blog_detail')
]