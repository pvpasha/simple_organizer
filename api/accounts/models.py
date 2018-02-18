from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
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
        user.save()
        return user


def dir_name(self, filename):
    url = "%s/%s" % (self.username, filename)
    return url


class OrganizerUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    avatar = ImageField(upload_to=dir_name, default='empty.jpg')
    jwt_token = models.CharField(max_length=512, blank=True)
    jwt_date = models.DateTimeField(blank=True, null=True)

    def image_thumb(self):
        im = get_thumbnail(self.avatar, '30x30', crop='center', quality=99)
        return u'<img src="%s"/>' % im.url

    image_thumb.short_description = 'Image'
    image_thumb.allow_tags = True

    def main_menu_avatar(self):
        return get_thumbnail(self.avatar, '50x50', crop='center', quality=99).url

    def main_menu_avatar_big(self):
        return get_thumbnail(self.avatar, '150x150', crop='center', quality=99).url

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
