from django.forms import ModelForm
from .models import News


class NewsForm(ModelForm):

    class Meta:
        model = News
        fields = ['title', 'photo', 'content', 'is_published', 'category']

    
