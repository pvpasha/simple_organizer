from django.db import models
from datetime import datetime
from accounts.models import OrganizerUser


class Category(models.Model):
    title = models.CharField(max_length=30)
    owner = models.ForeignKey(OrganizerUser, on_delete=models.CASCADE)

    def __str__(self):
        return "%d - %s" %(self.pk, self.title)

class AbstractTask(models.Model):
    owner = models.ForeignKey(OrganizerUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(default=datetime.now)
    category = models.ForeignKey(Category, models.SET_NULL, blank=True, null=True)


class ShortTask(AbstractTask):
    finished = models.BooleanField(default=False)


class Task(AbstractTask):
    finishing_date = models.DateTimeField(default=datetime.now)
    reminder = models.BooleanField(default=False)


class Event(AbstractTask):
    event_date = models.DateTimeField(default=datetime.now)

