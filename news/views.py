from django.shortcuts import render
from django.views import generic

from .models import News

from django.forms import modelformset_factory

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


def add_news(request):
    NewsFormSet = modelformset_factory(News, fields=('title', 'photo', 'content', 'is_published', 'category'))
    if request.method == 'POST':
        formset = NewsFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
    else:
        formset = NewsFormSet()
    return render(request, 'news/add.html', {'formset': formset})