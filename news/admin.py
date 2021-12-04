from typing import ClassVar
from django.contrib import admin

# Register your models here.
from .models import News, Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')



admin.site.register(News, NewsAdmin)
admin.site.register(Category)
