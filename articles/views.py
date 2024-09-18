from django.shortcuts import render, redirect
from django.views import View
from articles.forms import ArticleForm
from articles.models import Article

class ArticleView(View):
    form_class = ArticleForm
    template_name = 'articles.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        articles = Article.objects.all()
        context = {'form': form, 'articles': articles}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article-view')
        else:
            articles = Article.objects.all()
            context = {'form': form, 'articles': articles}
            return render(request, self.template_name, context)
