from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Client(models.Model):
    pass

class Person(models.Model):
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField("Фамилия", max_length=30)
    position = models.TextChoices('Должность', 'учредитель администратор сверки')
    email = models.EmailField("Почта", max_length = 254)
    phone = PhoneNumberField()