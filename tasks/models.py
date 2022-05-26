from django.db import models
from datetime import datetime, timedelta


# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=255, verbose_name='Наименование задачи')
    task_description = models.TextField(verbose_name='Описание')
    start_date = models.DateTimeField(default=datetime.today(), verbose_name='Дата начала')
    end_date = models.DateTimeField(default=datetime.today() + timedelta(days=1), verbose_name='Дата окончания')

    def __str__(self):
        return self.task_name
