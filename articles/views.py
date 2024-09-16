
from django.shortcuts import render
from articles.models import Article
from django.shortcuts import render


def home(request):
    if request.method == 'GET':
        infos = Article()
        context = {'infos': infos}
        return render(request, 'articles.html', context)

