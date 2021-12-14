from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .models import News
from.forms import NewsForm


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
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return reverse('news:index')
    else:
        form = NewsForm()
    return render(request, 'news/add.html', {'form': form})