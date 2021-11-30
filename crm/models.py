from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
PRICE = (
    ("Р", "Розница"),
    ("М", "Мелкий опт"),
    ("О", "Опт"),
    ("Д", "Дистрибьюция"),
)

class Client(models.Model):
    name = models.CharField("Название", max_length=50)
    persons = models.ManyToManyField(Person, blank=True)
    adress = models.CharField("Адрес", max_length=254, blank=True)
    phone = models.ForeignKey(Person, blank=True)
    function = models.BooleanField("Работает", default=True)
    about = models.TextField("Примечания", blank=True)
    date_joined = models.DateField()
    price_type = models.CharField("Тип цен", max_length=1, choices=PRICE)

    def __str__(self):
        return self.name



class Person(models.Model):
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField("Фамилия", max_length=30, blank=True)
    position = models.TextChoices('Должность', 'учредитель администратор сверки')
    email = models.EmailField("Почта", max_length = 254, blank=True)
    phone = PhoneNumberField(blank=True)
    function = models.BooleanField("Работает", default=True)
    enterprise = models.ManyToManyField(Client, blank=True)
    about = models.TextField("Примечания", blank=True)

    def __str__(self):
        return self.first_name