from django.contrib import admin

# Register your models here.
from .models import News, Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = 'updated_at'
    ordering = ('is_published', 'updated_at')



admin.site.register(News, NewsAdmin)
admin.site.register(Category)
