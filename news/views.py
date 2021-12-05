from django.shortcuts import render
from django.utils.translation import templatize
from django.views import generic

from .models import Category, News


class IndexView(generic.ListView):
    model = News
    template_name = "news/index.html"

    def get_queryset(self):
        return News.objects.filter(is_published=True)

class CategoryView(generic.ListView):
    model = News
    template_name = 'news/category.html'

    def get_queryset(self):
        return News.objects.filter(category__slug=self.kwargs['category_slug'], is_published=True)


class NewsView(generic.DetailView):
    model = News
    template_name = 'news/news.html'

    def get_queryset(self):
        return News.objects.filter(slug=self.kwargs['slug'], is_published=True)