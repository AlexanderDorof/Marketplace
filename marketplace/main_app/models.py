from datetime import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User as DjangoUser
from django.utils import timezone
from django.urls import reverse
from django.db import models
from dateutil.relativedelta import relativedelta


class Vehicle(models.Model):
    # consts
    COLOR_STYPE = (
        ('red', 'Красный'),
        ('blue', 'Синий'),
        ('green', 'Зеленый'),
        ('yellow', 'Желтый'),
        ('orange', 'Ораньжевый'),
        ('purple', 'Фиолетовый'),
        ('pink', 'Розовый'),
        ('brown', 'Коричневый'),
        ('gray', 'Серый'),
        ('teal', 'Бирюзовый'),
    )
    ENGINE_TYPE = (('Electricity', 'Электромобиль'), ('Oil', 'ДВС'))
    PERIOD = [
        (6, '6 месяцев'),
        (12, '12 месяцев'),
        (24, '2 года'),
        (36, '3 года'),
        (60, '5 лет'),
    ]

    brand = models.CharField(max_length=50, verbose_name='Марка')
    model = models.CharField(max_length=25, verbose_name='Модель')
    description = models.TextField(blank=True, default='Нет описания',
                                   help_text='Обязательно укажите поврежения автомобиля (при наличии)',
                                   verbose_name='Описание')
    used_car = models.BooleanField(default=False, verbose_name='Поддержанное т/с')
    distance = models.IntegerField(default=0, help_text='км', verbose_name='Пробег')
    year_produced = models.PositiveSmallIntegerField(blank=True, default=2000,
                                                     validators=[MaxValueValidator(datetime.now().year),
                                                                 MinValueValidator(1900)],
                                                     verbose_name='Год выпуска')
    guarantee = models.DateField(blank=True, verbose_name='Гарантийный срок')
    guarantee_period = models.SmallIntegerField(choices=PERIOD, default=12, verbose_name='Гарантийный период')
    engine_type = models.CharField(choices=ENGINE_TYPE, max_length=15, default='Oil',
                                   help_text='ДВС или электрокар', verbose_name='Тип двигателя')
    engine_power = models.PositiveSmallIntegerField(help_text='В лошадиных силах(л/с)', default=1600,
                                                    verbose_name='Мощность двигателя')
    color = models.CharField(blank=True, choices=COLOR_STYPE, max_length=15, default='red',
                             help_text='В соответствии с техпаспортом',
                             verbose_name='Цвет')
    price = models.PositiveSmallIntegerField(default=1000, help_text='В долларах ($)', verbose_name='Цена')

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        current_date = timezone.now().date()
        future_date = current_date + relativedelta(months=self.guarantee_period)
        self.guarantee = future_date
        super().save(*args, **kwargs)


class Car(Vehicle):
    # consts
    BODY_TYPE = (('Sedan', 'Седан'), ('Hatchback', 'Хэтчбэк'), ('Pickup', 'Пикап'), ('Cabrio', 'Кабриолет'))
    DRIVE_TYPE = (('Front', 'Переднеприводный'), ('Back', 'Заднеприводный'), ('Full', 'Полноприводный'))

    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name='URL slug')
    body_type = models.CharField(choices=BODY_TYPE, max_length=15, default='Sedan',
                                 help_text='В соответствии с техпаспортом',
                                 verbose_name='Тип кузова')
    drive_type = models.CharField(choices=DRIVE_TYPE, max_length=15, default='Front', verbose_name='Тип привода')
    photo = models.ImageField(blank=True, upload_to='photos/cars/%Y/%m/%d',
                              default='default_pic/no_image_available.jpg', verbose_name='Фотография')

    # related models
    seller = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Продавец')

    def __str__(self):
        return f'{self.brand} {self.model} {self.year_produced}'


    def get_absolute_url(self):
        return reverse('car_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


class Motocycle(Vehicle):
    # consts
    BODY_TYPE = (('Sport', 'Спортивный'), ('Classic', 'Классический'), ('Chopper', 'Чоппер'), ('Cross', 'Кросс'),
                 ('Enduro', 'Эндуро'), ('Cruiser', 'Круизер'), ('Scooter', 'Скутер'))

    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name='URL slug')
    body_type = models.CharField(choices=BODY_TYPE, max_length=15, default='Sport',
                                 help_text='В соответствии с техпаспортом',
                                 verbose_name='Типы')
    photo = models.ImageField(blank=True, upload_to='photos/motos/%Y/%m/%d',
                              default='default_pic/no_image_available.jpg', verbose_name='Фотография')

    # related models
    seller = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Продавец')

    def __str__(self):
        return f'{self.brand} {self.model} {self.year_produced}'

    def get_absolute_url(self):
        return reverse('moto_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Мотоцикл'
        verbose_name_plural = 'Мотоциклы'


class Item(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name='URL slug')
    description = models.TextField(blank=True, default='no description',
                                   help_text='Для чего предназначено, опишите плюсы и минусы',
                                   verbose_name='Описание')
    guarantee = models.DateField(blank=True, verbose_name='Гарантийный срок')
    price = models.DecimalField(max_digits=5, decimal_places=2, default=9.99, validators=[MinValueValidator(0)],
                                help_text='В долларах ($)', verbose_name='Цена')
    is_available = models.BooleanField(default=True, verbose_name='Имеется в наличии')

    class Meta:
        abstract = True


class ItemForCar(Item):
    cars_fit = models.ManyToManyField(Car, verbose_name='Подходит для:')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Доп для машины'
        verbose_name_plural = 'Допы для машины'


class ItemForMotorcycle(Item):
    motors_fit = models.ManyToManyField(Motocycle, verbose_name='Подходит для:')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Доп для мотоцикла'
        verbose_name_plural = 'Допы для мотоцикла'


class Service(models.Model):
    # consts
    SPECIALISTS = (
        ('Smirnov', 'Смирнов И.И.'), ('Sidorov', 'Сидоров А.К.'), ('Petrov', 'Петров Г.С.'), ('Anohin', 'Анохин Е.З.'))
    PERIOD = [
        (6, '6 месяцев'),
        (12, '12 месяцев'),
        (24, '2 года'),
        (36, '3 года'),
        (60, '5 лет'),
    ]

    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name='URL slug')
    description = models.TextField(blank=True, default='no description',
                                   help_text='Для чего предназначено, опишите плюсы и минусы',
                                   verbose_name='Описание')
    guarantee = models.DateField(blank=True, verbose_name='Гарантийный срок')
    guarantee_period = models.SmallIntegerField(choices=PERIOD, default=12, verbose_name='Гарантийный период')
    price = models.DecimalField(max_digits=5, decimal_places=2, default=9.99, validators=[MinValueValidator(0)],
                                help_text='В долларах ($)', verbose_name='Цена')
    is_available = models.BooleanField(default=True, verbose_name='Доступно сейчас')
    in_charge = models.CharField(max_length=255, default='Smirnov', verbose_name='Исполнитель', choices=SPECIALISTS)

    # related models
    cars_service = models.ManyToManyField(Car, blank=True, verbose_name='Подходит для:')
    motorcycles_service = models.ManyToManyField(Motocycle, blank=True, verbose_name='Подходит для:')

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        current_date = timezone.now().date()
        future_date = current_date + relativedelta(months=self.guarantee_period)
        self.guarantee = future_date
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def get_absolute_url(self):
        return reverse('service_url', kwargs={'slug': self.slug})


class User(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    second_name = models.CharField(blank=True, max_length=255, verbose_name='Отчество')
    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    age = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MaxValueValidator(120)],
                                           verbose_name='Возраст')
    photo = models.ImageField(blank=True, upload_to='photos/users/%Y/%m/%d',
                              default='default_pic/no_image_available.jpg', verbose_name='Фотография')
    date_registration = models.DateField(auto_now_add=True, verbose_name='Дата регистрации')
    blacklist = models.BooleanField(default=False, verbose_name='В черном списке')
    sold = models.PositiveSmallIntegerField(default=0, verbose_name='Продано автомобилей')

    # related models
    favorite = models.OneToOneField('Favorite', on_delete=models.CASCADE)
    user_django = models.OneToOneField(DjangoUser, on_delete=models.SET_NULL, related_name='user_django', blank=True,
                                       null=True)

    def __str__(self):
        return f"{self.surname} {self.name} {self.second_name if self.second_name else ''}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Favorite(models.Model):
    favorite_cars = models.ManyToManyField(Car, blank=True, verbose_name='Избранное автомобили')
    favorite_moto = models.ManyToManyField(Motocycle, blank=True, verbose_name='Избранное мотоциклы')

    def __str__(self):
        """if user created in admin panel and no favorite instance is associated with it - exception is raised"""
        try:
            user = User.objects.get(favorite__pk=self.pk)
            return f'Избранное: {user}'
        except ObjectDoesNotExist:
            return f'{self.pk}'

    class Meta:
        verbose_name = 'Список избранного'
        verbose_name_plural = 'Списки избранного'
