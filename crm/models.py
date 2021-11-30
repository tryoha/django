from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
PRICE = (
    ("Р", "Розница"),
    ("М", "Мелкий опт"),
    ("О", "Опт"),
    ("Д", "Дистрибьюция"),
)


class Person(models.Model):
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField("Фамилия", max_length=30, blank=True)
    PERSON_JOBS = [
        ("Учредитель", "Учредитель"),
        ("Администратор", "Администратор"),
        ("Сверки", "Сверки"),
    ]
    position = models.CharField('Должность', max_length=15, choices=PERSON_JOBS, blank=True)
    email = models.EmailField("Почта", max_length = 254, blank=True)
    phone = PhoneNumberField("Телефон", blank=True)
    exist = models.BooleanField("Работает", default=True)
    about = models.TextField("Примечания", blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Client(models.Model):
    name = models.CharField("Название", max_length=50)
    contact = models.ManyToManyField(Person, blank=True)
    adress = models.CharField("Адрес", max_length=254, blank=True)
    phone = PhoneNumberField("Телефон", blank=True)
    exist = models.BooleanField("Работает", default=True)
    about = models.TextField("Примечания", blank=True)
    date_joined = models.DateField("Начало работы", blank=True)
    price_type = models.CharField("Тип цен", max_length=1, choices=PRICE)

    def __str__(self):
        return self.name        