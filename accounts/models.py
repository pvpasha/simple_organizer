import jwt

from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from sorl.thumbnail import ImageField, get_thumbnail


class UserManager(BaseUserManager):

    def create_user(self, first_name, user_mail, password=None):
        if first_name is None:
            raise TypeError('Users must have a FirstName')
        if user_mail is None:
            raise TypeError('Users must have an email')
        user = self.model(first_name=first_name, user_mail=self.normalize_email(user_mail))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, user_mail, password):
        if password is None:
            raise TypeError('Superusers must have a password')
        user = self.create_user(first_name, user_mail, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


def dir_name(self, filename):
    url = "%s/%s" % (self.first_name, filename)
    return url


class OrganizerUser(AbstractBaseUser, PermissionsMixin):
    user_mail = models.EmailField(unique=True)
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    avatar = ImageField(upload_to=dir_name, default='empty.jpg')

    def image_thumb(self):
        im = get_thumbnail(self.avatar, '30x30', crop='center', quality=99)
        return u'<img src="%s"/>' % im.url

    image_thumb.short_description = 'Image'
    image_thumb.allow_tags = True

    def main_menu_avatar(self):
        return get_thumbnail(self.avatar, '50x50', crop='center', quality=99).url

    def main_menu_avatar_big(self):
        return get_thumbnail(self.avatar, '150x150', crop='center', quality=99).url

    USERNAME_FIELD = 'user_mail'
    REQUIRED_FIELDS = ['first_name']

    objects = UserManager()

    def __str__(self):
        return self.user_mail

    def get_full_name(self):
        return "%s %s" % (self.first_name, self.second_name)

    def get_short_name(self):
        return self.first_name

    @property         # is a succinct way of building a data descriptor that triggers function calls upon access to an attribute
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=3)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='H256')
        return token.decode('utf-8')


    def user_m_token(self):
        return "%s %s" % (self.user_mail, self.token)
