from django.db import models
from datetime import datetime

from accounts.models import OrganizerUser


class CategoryTask(models.Model):
    owner = models.ForeignKey(OrganizerUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class AbstractTask(models.Model):
    owner = models.ForeignKey(OrganizerUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    body = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class ShortTask(AbstractTask):
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Task(AbstractTask):
    category = models.ForeignKey(CategoryTask, models.SET_NULL, blank=True, null=True)
    starting_date = models.DateTimeField(default=datetime.now)
    finishing_date = models.DateTimeField(blank=True, null=True)
    finished = models.BooleanField(default=False)
    reminder_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Event(AbstractTask):
    event_date_start = models.DateTimeField(default=datetime.now)
    event_date_finish = models.DateTimeField(blank=True, null=True)
    reminder_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
