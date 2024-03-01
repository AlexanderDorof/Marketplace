# Generated by Django 4.2.9 on 2024-02-19 17:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_django',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_django', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='car',
            name='guarantee',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 2, 19, 17, 41, 38, 121134, tzinfo=datetime.timezone.utc), verbose_name='Гарантийный срок'),
        ),
        migrations.AlterField(
            model_name='item_for_car',
            name='guarantee',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 2, 19, 17, 41, 38, 122136, tzinfo=datetime.timezone.utc), verbose_name='Гарантийный срок'),
        ),
        migrations.AlterField(
            model_name='item_for_moto',
            name='guarantee',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 2, 19, 17, 41, 38, 122136, tzinfo=datetime.timezone.utc), verbose_name='Гарантийный срок'),
        ),
        migrations.AlterField(
            model_name='motocycle',
            name='guarantee',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 2, 19, 17, 41, 38, 121134, tzinfo=datetime.timezone.utc), verbose_name='Гарантийный срок'),
        ),
        migrations.AlterField(
            model_name='service',
            name='guarantee',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 2, 19, 17, 41, 38, 124134, tzinfo=datetime.timezone.utc), verbose_name='Гарантийный срок'),
        ),
    ]
