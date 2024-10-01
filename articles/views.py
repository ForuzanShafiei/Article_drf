from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from articles.models import Article
from articles.serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response_data = {
            "message": "مقاله جدید با موفقیت درج شد",
            "data": response.data
        }
        return Response(response_data, status=status.HTTP_201_CREATED, headers=response.headers)
