# Generated by Django 3.2.3 on 2021-06-04 18:47

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('api_cube', '0004_alter_solvetime_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='algorithm',
            name='moves',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(regex="^([FRULBDMESXYZfrulbd](\\'|2)? )*([FRULBDMESXYZfrulbd](\\'|2)?)$")]),
        ),
        migrations.AlterField(
            model_name='algorithm',
            name='slug',
            field=models.SlugField(primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')]),
        ),
        migrations.AlterField(
            model_name='alternative',
            name='alternative',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(regex="^([FRULBDMESXYZfrulbd](\\'|2)? )*([FRULBDMESXYZfrulbd](\\'|2)?)$")]),
        ),
    ]
