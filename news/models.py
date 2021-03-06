from django.db import models


class News(models.Model):
    title = models.CharField('Наименование', max_length=150, db_index=True)
    content = models.TextField('Контент', blank=True)
    created = models.DateTimeField('Дата публикации', auto_now_add=True)
    updated = models.DateTimeField('Обновлено', auto_now=True)
    photo = models.ImageField(
        'Картинка', upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    is_published = models.BooleanField('Опубликовано', default=True)
    category = models.ForeignKey(
        'Category', on_delete=models.PROTECT, null=True)
    slug = models.SlugField("Ссылка", unique=True,
                            max_length=50, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created']

    def get_absolute_url(self):
        from django.shortcuts import reverse
        return reverse('news:detail', kwargs={'category_slug': self.category.slug, 'slug': self.slug})


class Category(models.Model):
    title = models.CharField(
        max_length=150, db_index=True, verbose_name='Наименование')
    photo = models.ImageField(
        'Картинка', upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    slug = models.SlugField("Ссылка", unique=True,
                            max_length=50, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.shortcuts import reverse
        return reverse('news:category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Категория новости'
        verbose_name_plural = 'Категории новостей'
        ordering = ['title']
