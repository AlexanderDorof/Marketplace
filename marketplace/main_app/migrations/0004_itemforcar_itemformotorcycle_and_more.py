# Generated by Django 4.2.9 on 2024-03-09 12:32

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_car_body_type_alter_car_color_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemForCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='URL slug')),
                ('description', models.TextField(blank=True, default='no description', help_text='Для чего предназначено, опишите плюсы и минусы', verbose_name='Описание')),
                ('guarantee', models.DateField(blank=True, default=datetime.datetime(2024, 3, 9, 12, 32, 20, 787947, tzinfo=datetime.timezone.utc), verbose_name='Гарантийный срок')),
                ('price', models.DecimalField(decimal_places=2, default=9.99, help_text='В долларах ($)', max_digits=5, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена')),
                ('is_available', models.BooleanField(default=True, verbose_name='Имеется в наличии')),
            ],
            options={
                'verbose_name': 'Доп для машины',
                'verbose_name_plural': 'Допы для машины',
            },
        ),
        migrations.CreateModel(
            name='ItemForMotorcycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='URL slug')),
                ('description', models.TextField(blank=True, default='no description', help_text='Для чего предназначено, опишите плюсы и минусы', verbose_name='Описание')),
                ('guarantee', models.DateField(blank=True, default=datetime.datetime(2024, 3, 9, 12, 32, 20, 787947, tzinfo=datetime.timezone.utc), verbose_name='Гарантийный срок')),
                ('price', models.DecimalField(decimal_places=2, default=9.99, help_text='В долларах ($)', max_digits=5, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена')),
                ('is_available', models.BooleanField(default=True, verbose_name='Имеется в наличии')),
            ],
            options={
                'verbose_name': 'Доп для мотоцикла',
                'verbose_name_plural': 'Допы для мотоцикла',
            },
        ),
        migrations.RemoveField(
            model_name='item_for_moto',
            name='moto_fit',
        ),
        migrations.AlterField(
            model_name='car',
            name='body_type',
            field=models.CharField(choices=[('Sedan', 'Седан'), ('Hatchback', 'Хэтчбэк'), ('Pickup', 'Пикап'), ('Cabrio', 'Кабриолет')], default='Sedan', help_text='В соответствии с техпаспортом', max_length=15, verbose_name='Тип кузова'),
        ),
        migrations.AlterField(
            model_name='car',
            name='description',
            field=models.TextField(blank=True, default='Нет описания', help_text='Обязательно укажите поврежения автомобиля (при наличии)', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='car',
            name='guarantee',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 3, 9, 12, 32, 20, 786946, tzinfo=datetime.timezone.utc), verbose_name='Гарантийный срок'),
        ),
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, default='default_pic/no_image_available.jpg', upload_to='photos/cars/%Y/%m/%d', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='motocycle',
            name='body_type',
            field=models.CharField(choices=[('Sport', 'Спортивный'), ('Classic', 'Классический'), ('Chopper', 'Чоппер'), ('Cross', 'Кросс'), ('Enduro', 'Эндуро'), ('Cruiser', 'Круизер'), ('Scooter', 'Скутер')], default='Sport', help_text='В соответствии с техпаспортом', max_length=15, verbose_name='Типы'),
        ),
        migrations.AlterField(
            model_name='motocycle',
            name='description',
            field=models.TextField(blank=True, default='Нет описания', help_text='Обязательно укажите поврежения автомобиля (при наличии)', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='motocycle',
            name='guarantee',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 3, 9, 12, 32, 20, 786946, tzinfo=datetime.timezone.utc), verbose_name='Гарантийный срок'),
        ),
        migrations.AlterField(
            model_name='motocycle',
            name='photo',
            field=models.ImageField(blank=True, default='default_pic/no_image_available.jpg', upload_to='photos/motos/%Y/%m/%d', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='service',
            name='guarantee',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 3, 9, 12, 32, 20, 789946, tzinfo=datetime.timezone.utc), verbose_name='Гарантийный срок'),
        ),
        migrations.AlterField(
            model_name='service',
            name='in_charge',
            field=models.CharField(choices=[('Smirnov', 'Смирнов И.И.'), ('Sidorov', 'Сидоров А.К.'), ('Petrov', 'Петров Г.С.'), ('Anohin', 'Анохин Е.З.')], default='Smirnov', max_length=255, verbose_name='Исполнитель'),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, default='default_pic/no_image_available.jpg', upload_to='photos/users/%Y/%m/%d', verbose_name='Фотография'),
        ),
        migrations.DeleteModel(
            name='Item_for_car',
        ),
        migrations.DeleteModel(
            name='Item_for_moto',
        ),
        migrations.AddField(
            model_name='itemformotorcycle',
            name='motors_fit',
            field=models.ManyToManyField(to='main_app.motocycle', verbose_name='Подходит для:'),
        ),
        migrations.AddField(
            model_name='itemforcar',
            name='cars_fit',
            field=models.ManyToManyField(to='main_app.car', verbose_name='Подходит для:'),
        ),
    ]
