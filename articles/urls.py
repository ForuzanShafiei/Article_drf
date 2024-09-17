from django.urls import path
from articles.views import display_articles

urlpatterns = [
    path('', display_articles, name='article-list'),
]