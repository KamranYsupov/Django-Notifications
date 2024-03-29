from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from news import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.redirect_to_news_list),
    path('news/', include('news.urls')),
    path('users/', include('users.urls', namespace='users')),

    path('api/v1/', include('api.urls', namespace='api')),
    path('secret/', views.secret_page, name='secret_page')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)