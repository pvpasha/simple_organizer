from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager as _UserManager
from django.db import models
from django.utils import timezone
from sorl.thumbnail import ImageField, get_thumbnail


class UserManager(_UserManager):
    use_in_migrations = True

    def _create_user(self, user_mail, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not user_mail:
            raise ValueError('The given username must be set')
        user_mail = self.normalize_email(user_mail)
        user = self.model(user_mail=user_mail, is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, user_mail, password=None, **extra_fields):
        return self._create_user(user_mail, password, False, False, **extra_fields)

    def create_superuser(self, user_mail, password, **extra_fields):
        return self._create_user(user_mail, password, True, True, **extra_fields)

def dir_name(self, filename):
    url = "%s/%s" % (self.first_name, filename)
    return url


class OrganizerUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    user_mail = models.EmailField(unique=True)
    password = models.CharField(max_length=150)
    avatar = ImageField(upload_to=dir_name)

    def image_thumb(self):
        im = get_thumbnail(self.avatar, '150x150', crop='center', quality=99)
        return u'<img src="%s" width="50"/>' % im.url
    image_thumb.short_description = 'Image'
    image_thumb.allow_tags = True

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    objects = UserManager()
    USERNAME_FIELD = 'user_mail'
    REQUIRED_FIELDS = ['first_name', 'second_name']

    def get_full_name(self):
        return "%s %s" % (self.first_name, self.second_name)

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return "%d - %s" % (self.pk, self.user_mail)

    # def __str__(self):
    #     return u'User with Name %s %s and email %s' % (
    #         self.first_name, self.second_name, self.user_mail)
