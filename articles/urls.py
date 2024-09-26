from django.urls import path, include
from rest_framework.routers import DefaultRouter
from articles.views import ArticleViewSet

router = DefaultRouter()
router.register(r'', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
