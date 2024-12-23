from django.urls import path
from .views import CategoryListCreateView, PostListCreateView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view()),
    path('posts/', PostListCreateView.as_view()),
]
