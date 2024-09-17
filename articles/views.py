from django.shortcuts import render, redirect

from articles.forms.article_form import ArticleForm
from articles.models import Article


def article_view(request):
    if request.method == 'GET':
        form = ArticleForm()
        articles = Article.objects.all()
        context = {'form': form, 'articles': articles}
        return render(request, 'articles.html', context)

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            article = Article.objects.create(
                title=clean_data['title'],
                content=clean_data['content'],
                published_date=clean_data['published_date'],
            )
            article.save()
            context = {
                'form': form
            }
            return redirect('article-view')
