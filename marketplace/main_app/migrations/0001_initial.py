# Generated by Django 4.2.9 on 2024-02-04 08:44

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50, verbose_name='Марка')),
                ('model', models.CharField(max_length=25, verbose_name='Модель')),
                ('description', models.TextField(blank=True, default='Нет описания', help_text='Обязательно укажите поврежения автомобиля (при наличии)', verbose_name='Описание')),
                ('used_car', models.BooleanField(default=False, verbose_name='Поддержанное т/с')),
                ('distance', models.IntegerField(default=0, help_text='км', verbose_name='Пробег')),
                ('year_produced', models.PositiveSmallIntegerField(blank=True, default=2000, validators=[django.core.validators.MaxValueValidator(2024), django.core.validators.MinValueValidator(1900)], verbose_name='Год выпуска')),
                ('guarantee', models.DateField(blank=True, default=datetime.datetime(2024, 2, 4, 8, 44, 45, 526611, tzinfo=datetime.timezone.utc), verbose_name='Гарантицный срок')),
                ('engine_type', models.CharField(choices=[('E', 'Electricity'), ('Oil', 'Gasoline')], default='Electricity', help_text='ДВС или электрокар', max_length=15, verbose_name='Тип двигателя')),
                ('engine_power', models.PositiveSmallIntegerField(default=1600, help_text='В лошадиных силах(л/с)', verbose_name='Мощность двигателя')),
                ('color', models.CharField(blank=True, choices=[('Red', 'Red'), ('Blue', 'Blue'), ('Yellow', 'Yellow')], default='Red', help_text='В соответствии с техпаспортом', max_length=15, verbose_name='Цвет')),
                ('price', models.PositiveSmallIntegerField(default=1000, help_text='В долларах ($)', verbose_name='Цена')),
                ('body_type', models.CharField(choices=[('Sedan', 'Sedan'), ('Hatchback', 'Hatchback')], default='Sedan', help_text='В соответствии с техпаспортом', max_length=15, verbose_name='Тип кузова')),
                ('drive_type', models.CharField(choices=[('Front', 'Front-drive wheels'), ('Back', 'Back-drive wheels')], default='Front-drive wheels', max_length=15, verbose_name='Тип привода')),
                ('photo', models.ImageField(blank=True, default='default_pic/no_image_available.jpg', upload_to='photos/cars/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'Машина',
                'verbose_name_plural': 'Машины',
            },
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_cars', models.ManyToManyField(blank=True, to='main_app.car', verbose_name='Избранное автомобили')),
            ],
            options={
                'verbose_name': 'Список избранного',
                'verbose_name_plural': 'Списки избранного',
            },
        ),
        migrations.CreateModel(
            name='Motocycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50, verbose_name='Марка')),
                ('model', models.CharField(max_length=25, verbose_name='Модель')),
                ('description', models.TextField(blank=True, default='Нет описания', help_text='Обязательно укажите поврежения автомобиля (при наличии)', verbose_name='Описание')),
                ('used_car', models.BooleanField(default=False, verbose_name='Поддержанное т/с')),
                ('distance', models.IntegerField(default=0, help_text='км', verbose_name='Пробег')),
                ('year_produced', models.PositiveSmallIntegerField(blank=True, default=2000, validators=[django.core.validators.MaxValueValidator(2024), django.core.validators.MinValueValidator(1900)], verbose_name='Год выпуска')),
                ('guarantee', models.DateField(blank=True, default=datetime.datetime(2024, 2, 4, 8, 44, 45, 526611, tzinfo=datetime.timezone.utc), verbose_name='Гарантицный срок')),
                ('engine_type', models.CharField(choices=[('E', 'Electricity'), ('Oil', 'Gasoline')], default='Electricity', help_text='ДВС или электрокар', max_length=15, verbose_name='Тип двигателя')),
                ('engine_power', models.PositiveSmallIntegerField(default=1600, help_text='В лошадиных силах(л/с)', verbose_name='Мощность двигателя')),
                ('color', models.CharField(blank=True, choices=[('Red', 'Red'), ('Blue', 'Blue'), ('Yellow', 'Yellow')], default='Red', help_text='В соответствии с техпаспортом', max_length=15, verbose_name='Цвет')),
                ('price', models.PositiveSmallIntegerField(default=1000, help_text='В долларах ($)', verbose_name='Цена')),
                ('body_type', models.CharField(choices=[('Sport', 'Sport'), ('Classic', 'Classic')], default='Sport', help_text='В соответствии с техпаспортом', max_length=15, verbose_name='Типы')),
                ('photo', models.ImageField(blank=True, default='default_pic/no_image_available.jpg', upload_to='photos/motos/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'Мотоцикл',
                'verbose_name_plural': 'Мотоциклы',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('second_name', models.CharField(blank=True, max_length=255, verbose_name='Отчество')),
                ('surname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(120)], verbose_name='Возраст')),
                ('photo', models.ImageField(blank=True, default='default_pic/no_image_available.jpg', upload_to='photos/users/%Y/%m/%d')),
                ('date_registration', models.DateField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('blacklist', models.BooleanField(default=False, verbose_name='В черном списке')),
                ('sold', models.PositiveSmallIntegerField(default=0, verbose_name='Продано автомобилей')),
                ('favorite', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.favorite')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, default='no description', help_text='Для чего предназначено, опишите плюсы и минусы', verbose_name='Описание')),
                ('guarantee', models.DateField(blank=True, default=datetime.datetime(2024, 2, 4, 8, 44, 45, 528609, tzinfo=datetime.timezone.utc), verbose_name='Гарантицный срок')),
                ('price', models.DecimalField(decimal_places=2, default=9.99, help_text='В долларах ($)', max_digits=5, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена')),
                ('is_available', models.BooleanField(default=True, verbose_name='Доступно сейчас')),
                ('in_charge', models.CharField(default='Смирнов И.И.', max_length=255, verbose_name='Исполнитель')),
                ('cars_service', models.ManyToManyField(blank=True, to='main_app.car', verbose_name='Подходит для:')),
                ('motorcycles_service', models.ManyToManyField(blank=True, to='main_app.motocycle', verbose_name='Подходит для:')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.AddField(
            model_name='motocycle',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.user', verbose_name='Продавец'),
        ),
        migrations.CreateModel(
            name='Item_for_moto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, default='no description', help_text='Для чего предназначено, опишите плюсы и минусы', verbose_name='Описание')),
                ('guarantee', models.DateField(blank=True, default=datetime.datetime(2024, 2, 4, 8, 44, 45, 527610, tzinfo=datetime.timezone.utc), verbose_name='Гарантицный срок')),
                ('price', models.DecimalField(decimal_places=2, default=9.99, help_text='В долларах ($)', max_digits=5, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена')),
                ('is_available', models.BooleanField(default=True, verbose_name='Имеется в наличии')),
                ('moto_fit', models.ManyToManyField(to='main_app.motocycle', verbose_name='Подходит для:')),
            ],
            options={
                'verbose_name': 'Доп для мотоцикла',
                'verbose_name_plural': 'Допы для мотоцикла',
            },
        ),
        migrations.CreateModel(
            name='Item_for_car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, default='no description', help_text='Для чего предназначено, опишите плюсы и минусы', verbose_name='Описание')),
                ('guarantee', models.DateField(blank=True, default=datetime.datetime(2024, 2, 4, 8, 44, 45, 527610, tzinfo=datetime.timezone.utc), verbose_name='Гарантицный срок')),
                ('price', models.DecimalField(decimal_places=2, default=9.99, help_text='В долларах ($)', max_digits=5, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена')),
                ('is_available', models.BooleanField(default=True, verbose_name='Имеется в наличии')),
                ('car_fit', models.ManyToManyField(to='main_app.car', verbose_name='Подходит для:')),
            ],
            options={
                'verbose_name': 'Доп для машины',
                'verbose_name_plural': 'Допы для машины',
            },
        ),
        migrations.AddField(
            model_name='favorite',
            name='favorite_moto',
            field=models.ManyToManyField(blank=True, to='main_app.motocycle', verbose_name='Избранное мотоциклы'),
        ),
        migrations.AddField(
            model_name='car',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.user', verbose_name='Продавец'),
        ),
    ]
