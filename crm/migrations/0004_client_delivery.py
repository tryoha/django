# Generated by Django 3.2.9 on 2021-11-30 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20211130_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='delivery',
            field=models.CharField(blank=True, choices=[('Север и цетр', 'вторник, четверг, суббота'), ('Юг', 'понедельник, среда, пятница'), ('Пригород', 'среда'), ('Регион', 'регион')], max_length=12, verbose_name='Развозка'),
        ),
    ]