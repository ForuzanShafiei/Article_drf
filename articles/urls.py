from django.urls import path
from articles.views import home

urlpatterns = [
    path('', home, name='article-list'),
]