from django.db import models
from datetime import date, datetime, timedelta
from accounts.models import OrganizerUser


class Category(models.Model):
    title = models.CharField(max_length=30)
    owner = models.ForeignKey(OrganizerUser, on_delete=models.CASCADE)

    def __str__(self):
        return "%d - %s" %(self.pk, self.title)



class ShortTask(models.Model):
    owner = models.ForeignKey(OrganizerUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(default=datetime.now)
    finished = models.BooleanField(default=False)
    category = models.ForeignKey(Category, models.SET_NULL, blank=True, null=True)




class Task(models.Model):
    owner = models.ForeignKey(OrganizerUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(default=datetime.now)
    finishing_date = models.DateTimeField(default=datetime.now)
    reminder = models.BooleanField(default=False)
    category = models.ForeignKey(Category, models.SET_NULL, blank=True, null=True)


class Event(models.Model):
    owner = models.ForeignKey(OrganizerUser, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=datetime.now)
    title = models.CharField(max_length=30)
    body = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, models.SET_NULL, blank=True, null=True)
    event_date = models.DateTimeField(default=datetime.now)






