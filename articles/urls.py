from django.urls import path
from articles.views import ArticleView

urlpatterns = [
    path('', ArticleView.as_view(), name='article-view'),  # فراخوانی متد as_view() برای ویوی کلاس‌بنیاد
]
