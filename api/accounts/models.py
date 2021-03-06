from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from django.db import models
from sorl.thumbnail import ImageField, get_thumbnail


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users must have a FirstName')
        if email is None:
            raise TypeError('Users must have an email')
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('SuperUsers must have a password')
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()
        return user


def dir_name(self, filename):
    url = '%s/%s_%s' % (settings.AVATAR_DIR, self.email, filename)
    return url


class OrganizerUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    avatar = ImageField(upload_to=dir_name, default='empty.png')
    jwt_token = models.CharField(max_length=512, blank=True)
    jwt_date = models.DateTimeField(blank=True, null=True)

    def image_thumb(self):
        im = get_thumbnail(self.avatar, '30x30', crop='center', quality=99)
        return u'<img src="%s"/>' % im.url

    def main_menu_avatar(self):
        pic = get_thumbnail(self.avatar, '50x50', crop='center', quality=99)
        return u'http://localhost:8000%s' % pic.url

    def main_menu_avatar_big(self):
        pic = get_thumbnail(self.avatar, '100x100', crop='center', quality=99)
        return u'http://localhost:8000%s' % pic.url

    image_thumb.short_description = 'Image'
    image_thumb.allow_tags = True

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return "%s %s" % (self.username, self.second_name)

    def get_short_name(self):
        return self.username

    def get_user_email(self):
        return self.email
