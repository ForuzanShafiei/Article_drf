from django.shortcuts import render, redirect
from django.views import View
from articles.forms import ArticleForm
from articles.models import Article

class ArticleView(View):
    form_class = ArticleForm
    template_name = 'articles.html'

    def get(self, request, *args, **kwargs):
        # نمایش فرم خالی و لیست مقالات
        form = self.form_class()
        articles = Article.objects.all()
        context = {'form': form, 'articles': articles}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # دریافت داده‌های فرم با متد POST
        form = self.form_class(request.POST)
        if form.is_valid():  # اعتبارسنجی فرم
            form.save()  # ذخیره فرم در دیتابیس
            return redirect('article-view')  # پس از ذخیره موفق، بازگشت به صفحه اصلی
        else:
            # اگر فرم نامعتبر بود، دوباره فرم و لیست مقالات را نمایش می‌دهیم
            articles = Article.objects.all()
            context = {'form': form, 'articles': articles}
            return render(request, self.template_name, context)
