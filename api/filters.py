from django_filters.rest_framework import DjangoFilterBackend
from .models import Post
from rest_framework.generics import ListAPIView


class PostModelViewSet(ListAPIView):
    queryset = Post.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'category']
