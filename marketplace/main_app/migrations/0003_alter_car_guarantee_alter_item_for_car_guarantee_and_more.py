# Generated by Django 5.0.1 on 2024-02-18 19:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_car_guarantee_alter_item_for_car_guarantee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='guarantee',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 2, 18, 19, 40, 54, 164634, tzinfo=datetime.timezone.utc), verbose_name='Гарантийный срок'),
        ),
        migrations.AlterField(
            model_name='item_for_car',
            name='guarantee',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 2, 18, 19, 40, 54, 165543, tzinfo=datetime.timezone.utc), verbose_name='Гарантийный срок'),
        ),
        migrations.AlterField(
            model_name='item_for_moto',
            name='guarantee',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 2, 18, 19, 40, 54, 165543, tzinfo=datetime.timezone.utc), verbose_name='Гарантийный срок'),
        ),
        migrations.AlterField(
            model_name='motocycle',
            name='guarantee',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 2, 18, 19, 40, 54, 164634, tzinfo=datetime.timezone.utc), verbose_name='Гарантийный срок'),
        ),
        migrations.AlterField(
            model_name='service',
            name='guarantee',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 2, 18, 19, 40, 54, 166706, tzinfo=datetime.timezone.utc), verbose_name='Гарантийный срок'),
        ),
    ]
