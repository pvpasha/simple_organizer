from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=20)
    forename = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    birthday = models.DateField(default=date.today)
    add_reminder = models.BooleanField(default=False)

    #add birthday to reminder
def add_reminder(self):
    pass