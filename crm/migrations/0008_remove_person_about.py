# Generated by Django 3.2.9 on 2021-12-01 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_auto_20211201_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='about',
        ),
    ]