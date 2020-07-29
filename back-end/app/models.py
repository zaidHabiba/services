from django.contrib.auth.models import User as UserBase
from django.contrib.auth.base_user import AbstractBaseUser

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class BaseModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, blank=True, null=True)


class Image(BaseModel):
    file = models.FileField(upload_to="images")


class ChangeLog(BaseModel):
    descriptions = models.TextField(default=None, blank=True, null=True)


class Country(BaseModel):
    name = models.CharField(max_length=64)
    flag = models.CharField(max_length=5)
    zip_code = models.CharField(max_length=10)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True, null=True, blank=True)
    first_name = models.CharField(_('first name'), max_length=32, blank=True)
    last_name = models.CharField(_('last name'), max_length=32, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=True)
    second_name = models.CharField(max_length=32, blank=True)
    middle_name = models.CharField(max_length=32, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, null=True)
    avatar = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    @property
    def username(self):
        return self.email

    @property
    def full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return self.email


class IpLogin(BaseModel):
    start = models.GenericIPAddressField(unpack_ipv4=False)
    end = models.GenericIPAddressField(unpack_ipv4=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="access_ips")
