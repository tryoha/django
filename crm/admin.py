from django.contrib import admin

# Register your models here.
from .models import Person, Client


admin.site.register(Person)
admin.site.register(Client)