# Generated by Django 3.1.2 on 2020-10-15 19:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('url', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message='Only alphanumeric, dashes, and underscores allowed', regex='^[a-zA-Z0-9_\\-]+$')])),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('url', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message='Only alphanumeric, dashes, and underscores allowed', regex='^[a-zA-Z0-9_\\-]+$')])),
                ('courses', models.ManyToManyField(related_name='subject', to='courses.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('teacher', models.CharField(blank=True, max_length=100)),
                ('url', models.URLField(max_length=300)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
    ]
