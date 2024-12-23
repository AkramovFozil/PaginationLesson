from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from .serializers import PostSerializer, CategorySerializer


class MyCategoryPagination(PageNumberPagination):
    page_size = 5


class MyPostNumberPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 100
