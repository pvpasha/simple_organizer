from django.db import models

from accounts.models import OrganizerUser


class PasswordOrganizer(models.Model):
    owner = models.ForeignKey(OrganizerUser, on_delete=models.CASCADE)
    resource_url = models.CharField(max_length=250)
    password_res = models.CharField(max_length=250)
