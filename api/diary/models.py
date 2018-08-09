from django.db import models

from accounts.models import OrganizerUser


class Diary(models.Model):
    owner = models.ForeignKey(OrganizerUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
