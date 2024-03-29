from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .news.views import NewsAPIViewSet
from .notifications.views import NotificationAPIViewSet
from .users.views import UserAPIViewSet

app_name = 'api'

router = DefaultRouter()

router.register(r'news', NewsAPIViewSet)
router.register(r'notifications', NotificationAPIViewSet)
router.register(r'users', UserAPIViewSet)


urlpatterns = [
    path('', include(router.urls)),
]