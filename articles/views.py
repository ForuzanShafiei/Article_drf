from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from articles.forms.article_form import ArticleForm
from articles.models import Article


@require_GET
def display_articles(request):
    articles = Article.objects.all()
    return render(request,  'articles.html', {'articles': articles})


@require_POST
def upload_article(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        clean_data = form.cleaned_data
        article = Article.objects.create(
            title=clean_data['title'],
            content=clean_data['content'],
            published_date=clean_data['published_date'],
        )
        return redirect('display_user')
    else:
        return render(request, 'articles.html', {'form': form})