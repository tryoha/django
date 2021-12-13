# Generated by Django 3.2.9 on 2021-12-03 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0010_alter_client_price_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterField(
            model_name='client',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Ссылка'),
        ),
    ]