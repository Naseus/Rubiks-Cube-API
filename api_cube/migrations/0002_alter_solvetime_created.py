# Generated by Django 3.2.3 on 2021-05-25 18:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api_cube', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solvetime',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
        ),
    ]
