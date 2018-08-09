from django.db import models

from accounts.models import OrganizerUser as User


class Contact(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20, unique=True)
    email_address = models.EmailField(blank=True, null=True)
    home_address = models.CharField(max_length=250, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    add_reminder = models.BooleanField(default=False)
