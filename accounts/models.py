from django.db import models

# Create your models here.


class OrganizerUser(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    user_mail = models.EmailField()
    user_pass = models.CharField(max_length=15)
