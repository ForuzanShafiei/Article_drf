from django.urls import path
from articles.views import article_view

urlpatterns = [
    path('', article_view, name='article-view'),
]