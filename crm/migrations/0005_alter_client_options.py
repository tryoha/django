# Generated by Django 4.0 on 2022-01-04 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_alter_person_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'permissions': [('special_status', 'Can view clients')], 'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
    ]
