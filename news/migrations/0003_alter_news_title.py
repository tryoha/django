# Generated by Django 4.0 on 2022-01-15 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_category_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Наименование'),
        ),
    ]