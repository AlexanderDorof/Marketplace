from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.utils import timezone


class Vehicle(models.Model):
    ColorsType = [("Red", "Red"), ("Blue", "Blue"), ("Yellow", "Yellow")]
    EngineType = [("E", "Electricity"), ("Oil", "Gasoline")]
    brand = models.CharField(max_length=50, verbose_name='Марка')
    model = models.CharField(max_length=25, verbose_name='Модель')
    description = models.TextField(blank=True, default='Нет описания',
                                   help_text="Обязательно укажите поврежения автомобиля (при наличии)",
                                   verbose_name='Описание')
    used_car = models.BooleanField(default=False, verbose_name='Поддержанное т/с')
    distance = models.IntegerField(default=0, help_text="км", verbose_name='Пробег')
    year_produced = models.PositiveSmallIntegerField(blank=True, default=2000,
                                                     validators=[MaxValueValidator(datetime.now().year),
                                                                 MinValueValidator(1900)],
                                                     verbose_name='Год выпуска')
    guarantee = models.DateField(blank=True, default=timezone.now(), verbose_name='Гарантийный срок')
    engine_type = models.CharField(choices=EngineType, max_length=15, default=EngineType[0][1],
                                   help_text="ДВС или электрокар", verbose_name='Тип двигателя')
    engine_power = models.PositiveSmallIntegerField(help_text="В лошадиных силах(л/с)", default=1600,
                                                    verbose_name='Мощность двигателя')
    color = models.CharField(blank=True, choices=ColorsType, max_length=15, default=ColorsType[0][1],
                             help_text="В соответствии с техпаспортом",
                             verbose_name='Цвет')
    price = models.PositiveSmallIntegerField(default=1000, help_text="В долларах ($)", verbose_name='Цена')

    class Meta:
        abstract = True


class Car(Vehicle):
    BodyType = [("Sedan", "Sedan"), ("Hatchback", "Hatchback")]
    DriveType = [("Front", "Front-drive wheels"), ("Back", "Back-drive wheels")]
    body_type = models.CharField(choices=BodyType, max_length=15, default=BodyType[0][1],
                                 help_text="В соответствии с техпаспортом",
                                 verbose_name='Тип кузова')
    drive_type = models.CharField(choices=DriveType, max_length=15, default=DriveType[0][1], verbose_name='Тип привода')
    photo = models.ImageField(blank=True, upload_to="photos/cars/%Y/%m/%d",
                              default="default_pic/no_image_available.jpg")
    seller = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Продавец')


    def __str__(self):
        return f"{self.brand} {self.model} {self.year_produced}"

    def get_absolute_url(self):
        return reverse('car_url', kwargs={'id': self.id, 'brand': self.brand})

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"


class Motocycle(Vehicle):
    BodyType = [("Sport", "Sport"), ("Classic", "Classic")]
    body_type = models.CharField(choices=BodyType, max_length=15, default=BodyType[0][1],
                                 help_text="В соответствии с техпаспортом",
                                 verbose_name='Типы')
    photo = models.ImageField(blank=True, upload_to="photos/motos/%Y/%m/%d",
                              default="default_pic/no_image_available.jpg")
    seller = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Продавец')

    def __str__(self):
        return f"{self.brand} {self.model} {self.year_produced}"

    def get_absolute_url(self):
        return reverse('car_url', kwargs={'id': self.id, 'brand': self.brand})

    class Meta:
        verbose_name = "Мотоцикл"
        verbose_name_plural = "Мотоциклы"


class Item(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, default='no description',
                                   help_text="Для чего предназначено, опишите плюсы и минусы",
                                   verbose_name='Описание')
    guarantee = models.DateField(blank=True, default=timezone.now(), verbose_name='Гарантийный срок')
    price = models.DecimalField(max_digits=5, decimal_places=2, default=9.99, validators=[MinValueValidator(0)],
                                help_text="В долларах ($)", verbose_name='Цена')
    is_available = models.BooleanField(default=True, verbose_name='Имеется в наличии')

    class Meta:
        abstract = True


class Item_for_car(Item):
    car_fit = models.ManyToManyField(Car, verbose_name='Подходит для:')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Доп для машины"
        verbose_name_plural = "Допы для машины"


class Item_for_moto(Item):
    moto_fit = models.ManyToManyField(Motocycle, verbose_name='Подходит для:')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Доп для мотоцикла"
        verbose_name_plural = "Допы для мотоцикла"


class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, default='no description',
                                   help_text="Для чего предназначено, опишите плюсы и минусы",
                                   verbose_name='Описание')
    guarantee = models.DateField(blank=True, default=timezone.now(), verbose_name='Гарантийный срок')
    price = models.DecimalField(max_digits=5, decimal_places=2, default=9.99, validators=[MinValueValidator(0)],
                                help_text="В долларах ($)", verbose_name='Цена')
    is_available = models.BooleanField(default=True, verbose_name='Доступно сейчас')
    in_charge = models.CharField(max_length=255, default="Смирнов И.И.", verbose_name='Исполнитель')
    cars_service = models.ManyToManyField(Car, blank=True, verbose_name='Подходит для:')
    motorcycles_service = models.ManyToManyField(Motocycle, blank=True, verbose_name='Подходит для:')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class User(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    second_name = models.CharField(blank=True, max_length=255, verbose_name='Отчество')
    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    age = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MaxValueValidator(120)],
                                           verbose_name='Возраст')
    photo = models.ImageField(blank=True, upload_to="photos/users/%Y/%m/%d",
                              default="default_pic/no_image_available.jpg")
    date_registration = models.DateField(auto_now_add=True, verbose_name='Дата регистрации')
    blacklist = models.BooleanField(default=False, verbose_name='В черном списке')
    sold = models.PositiveSmallIntegerField(default=0, verbose_name='Продано автомобилей')
    favorite = models.OneToOneField('Favorite', on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(default='asdsasadasd@gmail.com')
    def __str__(self):
        return f"{self.surname} {self.name} {self.second_name if self.second_name else ''}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Favorite(models.Model):
    favorite_cars = models.ManyToManyField(Car, blank=True, verbose_name='Избранное автомобили')
    favorite_moto = models.ManyToManyField(Motocycle, blank=True, verbose_name='Избранное мотоциклы')

    def __str__(self):
        try:
            user = User.objects.get(favorite__pk=self.pk)
            return f"Избранное: {user}"
        except ObjectDoesNotExist:
            return f"{self.pk}"

    class Meta:
        verbose_name = "Список избранного"
        verbose_name_plural = "Списки избранного"
