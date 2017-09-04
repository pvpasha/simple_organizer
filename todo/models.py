from django.db import models


class ToDo(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(blank=True, null=True)
    owner = models.EmailField()
    finished = models.BooleanField(default=False)
