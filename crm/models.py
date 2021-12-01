from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

PRICE = (
    ("И", "Интернет"),
    ("Р", "Розница"),
    ("М", "Мелкий опт"),
    ("О", "Опт"),
    ("Д", "Дистрибьюция"),
)

DELIVERY_REGIONS = (
    ("Всеволожск", "ежедневно"),
    ("Север и цетр", "вторник, четверг, суббота"),
    ("Юг", "понедельник, среда, пятница"),
    ("Пригород", "среда"),
    ("Регион", "регион"),
)

CLIENT_STATUS = (
    ("Новый", "Новый"),
    ("Текущий", "Текущий"),
    ("Потенциальный", "Потенциальный"),
    ("Контакт из почты", "Контакт из почты"),
    ("Архив", "Архив"),
)


class Client(models.Model):
    name = models.CharField("Название", max_length=50)
    slug = models.SlugField("Ссылка", unique=True, max_length=50)
    adress = models.CharField("Адрес", max_length=254, blank=True)
    status = models.CharField("Cтатус", max_length=20,
                              choices=CLIENT_STATUS, blank=True)
    date_joined = models.DateField("Начало работы", blank=True)
    price_type = models.CharField(
        "Тип цен", max_length=1, choices=PRICE, blank=True)
    delivery = models.CharField(
        "Развозка", max_length=12, choices=DELIVERY_REGIONS, blank=True)
    about = models.TextField("Примечания", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Person(models.Model):
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField("Фамилия", max_length=30, blank=True)
    PERSON_JOBS = [
        ("Учредитель", "Учредитель"),
        ("Администратор", "Администратор"),
        ("Сверки", "Сверки"),
    ]
    contact = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True)
    position = models.CharField(
        'Должность', max_length=15, choices=PERSON_JOBS, blank=True)
    email = models.EmailField("Почта", max_length=254, blank=True)
    phone = PhoneNumberField("Телефон", blank=True)
    exist = models.BooleanField("Работает", default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'