from django.urls import path
from . import views


urlpatterns = [
    path('', views.NewsList.as_view(), name='news_list'),
    path('<int:obj_id>/', views.read_news_obj, name='read_news_obj'),
    path('add/', views.add_news_obj, name='add_news_obj'),
    path('change/<int:obj_id>/', views.change_news_obj, name='change_news_obj'),
]