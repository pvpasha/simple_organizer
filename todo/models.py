from django.db import models
from django.utils import timezone, duration


class ToDo(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(blank=True, null=True)
    owner = models.EmailField()
    finished = models.BooleanField(default=False)


class Task(models.Model):
    task_text = models.TextField(max_length=30)
    time_for_work = models.DurationField
    finished_time = models.DateTimeField
    check_task = models.BooleanField(default=False)


class Contact(models.Model):
    name_c = models.CharField(max_length=20)
    forename_c = models.CharField(max_length=20)
    phone_num = models.IntegerField
    birthday_c = models.DateField

