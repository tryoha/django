from django.contrib.sitemaps import Sitemap
from .models import News


class NewsSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return News.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated

