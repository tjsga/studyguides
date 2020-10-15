# Generated by Django 3.1.2 on 2020-10-15 19:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='url',
        ),
        migrations.AlterField(
            model_name='subject',
            name='url',
            field=models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message='Only alphanumeric, dashes, and underscores allowed', regex='^[a-zA-Z0-9_\\-]+$')], verbose_name='URL'),
        ),
    ]