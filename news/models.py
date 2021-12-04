from django.db import models


class News(models.Model):
    title = models.CharField('Наименование', max_length=150)
    content = models.TextField('Контент', blank=True)
    created_at = models.DateTimeField('Дата публикации', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now_add=True)
    photo = models.ImageField('Картинка', upload_to='media/photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField('Опубликовано', default=True)
    category = models.ForeignKey(
        'Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(
        max_length=150, db_index=True, verbose_name='Наименование')
    photo = models.ImageField('Картинка', upload_to='photos/%Y/%m/%d/', null=True)
    

    def __str__(self):
        return self.title        

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
