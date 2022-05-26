# Generated by Django 4.0.4 on 2022-05-26 19:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=255, verbose_name='Наименование задачи')),
                ('task_description', models.TextField(verbose_name='Описание')),
                ('start_date', models.DateTimeField(default=datetime.datetime(2022, 5, 26, 22, 43, 56, 810726), verbose_name='Дата начала')),
                ('end_date', models.DateTimeField(default=datetime.datetime(2022, 5, 27, 22, 43, 56, 810726), verbose_name='Дата окончания')),
            ],
        ),
    ]