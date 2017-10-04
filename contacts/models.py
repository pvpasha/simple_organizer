from django.db import models
from datetime import date

from accounts.models import OrganizerUser


class Contact(models.Model):
    owner = models.ForeignKey(OrganizerUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    birthday = models.DateField(blank=True, null=True, verbose_name="Contact's birthday")
    add_reminder = models.BooleanField(default=False)

    # TODO add birthday to reminder
def add_reminder(self):
    pass