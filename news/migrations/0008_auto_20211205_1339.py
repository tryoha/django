# Generated by Django 3.2.9 on 2021-12-05 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20211205_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Ссылка'),
        ),
    ]
