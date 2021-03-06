from django.contrib import admin

from .models import Person, Client


class PersonInlne(admin.TabularInline):
    model = Person
    extra = 1


class ClientAdmin(admin.ModelAdmin):

    inlines = [PersonInlne]
    list_display = ('name', 'status', 'price_type', 'delivery')
    search_fields = ['name']
    list_filter = ('status', 'price_type', 'delivery')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Client, ClientAdmin)
