# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-05 20:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('robot', models.CharField(max_length=20)),
                ('task_number', models.FloatField()),
                ('task1_speed', models.FloatField()),
                ('task1_duration', models.FloatField()),
                ('task1_mode', models.CharField(max_length=20)),
                ('task1_command', models.CharField(max_length=20)),
                ('task1_num', models.FloatField()),
                ('task1_char', models.CharField(max_length=20)),
                ('task1_bool', models.BooleanField()),
                ('task2_speed', models.FloatField()),
                ('task2_duration', models.FloatField()),
                ('task2_mode', models.CharField(max_length=20)),
                ('task2_command', models.CharField(max_length=20)),
                ('task2_num', models.FloatField()),
                ('task2_char', models.CharField(max_length=20)),
                ('task2_bool', models.BooleanField()),
                ('task3_speed', models.FloatField()),
                ('task3_duration', models.FloatField()),
                ('task3_mode', models.CharField(max_length=20)),
                ('task3_command', models.CharField(max_length=20)),
                ('task3_num', models.FloatField()),
                ('task3_char', models.CharField(max_length=20)),
                ('task3_bool', models.BooleanField()),
                ('task_loop', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('controler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]