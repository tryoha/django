from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from .models import News
from .forms import NewsForm


class IndexView(generic.ListView):
    model = News
    template_name = "news/index.html"
    paginate_by = 3

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class CategoryView(generic.ListView):
    model = News
    template_name = 'news/category.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.kwargs['category_slug']
        return context

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
            new = form.save()
            return HttpResponseRedirect(new.get_absolute_url())
    else:
        form = NewsForm()
    return render(request, 'news/add.html', {'form': form})