from django.contrib import admin

# Register your models here.
from .models import News, Category

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created', 'updated', 'is_published')
    list_display_links = ('id', 'title',)
    list_filter = ('category', 'created', 'updated', 'is_published')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = 'updated'
    ordering = ('is_published', 'updated')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}