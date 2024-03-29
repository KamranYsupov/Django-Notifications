from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination

from .serializers import NewsSerializer
from news.models import News


class NewsAPIViewSet(ModelViewSet):
    queryset = News.objects.select_related('author')
    serializer_class = NewsSerializer

    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
