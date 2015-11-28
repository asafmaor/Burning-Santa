from django.db import models
from django.contrib.auth.models import User


class SantaBase(models.Model):
    class Meta:
        abstract = True
        app_label = 'santa'


class SantaUser(User):
    playa_name = models.CharField(max_length=100, null=True)
    willing_to_get = models.BinaryField(default=True)
    santa_to = models.ForeignKey('SantaUser', null=True)


class Address(SantaBase):
    user = models.ForeignKey(SantaUser, related_name='address')
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    zipcode = models.CharField(max_length=32, null=True)


class GiftingLog(SantaBase):
    user = models.ForeignKey(SantaUser, related_name='gifts')
    creation_time = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=100, null=True)

