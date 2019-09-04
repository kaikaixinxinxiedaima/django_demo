from django.urls import path, include

from blog import views

urlpatterns = [
    path('article', views.ArticleListHandle.as_view(), name='article_list'),
    path('article/<pk>', views.ArticleDetailHandle.as_view(), name='article_detail'),
]