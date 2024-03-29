from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.pagination import PageNumberPagination

from notifications.models import Notification
from .serializers import NotificationSerializer


class NotificationAPIViewSet(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    permission_classes = IsAdminUser,
    pagination_class = PageNumberPagination
