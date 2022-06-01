import django.utils.timezone
from django.db import models
from datetime import datetime, timedelta
from accounts.models import Account


# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=255, verbose_name='Наименование задачи')
    task_description = models.TextField(verbose_name='Описание')
    start_date = models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата начала')
    end_date = models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата окончания')
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_name
