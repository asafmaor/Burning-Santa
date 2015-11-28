from django.db import models
from django.contrib.auth.models import User


class SantaBase(models.Model):
    class Meta:
        abstract = True
        app_label = 'santa'


class SantaUser(SantaBase):
    django_user = models.OneToOneField(User)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    _email = models.EmailField(db_column='email')
    is_signed_in = models.BinaryField(default=False)
    playa_name = models.CharField(max_length=100, null=True)
    willing_to_get = models.BinaryField(default=True)
    santa_to = models.ForeignKey('SantaUser', null=True)
    what_makes_you_happy = models.CharField(max_length=100, null=True)
    what_makes_you_sad = models.CharField(max_length=100, null=True)
    what_power_ranger_are_you = models.CharField(max_length=100, null=True)

    @property
    def email(self):
        return self._email

    @email.setter
    def set_email(self, email):
        self._email = email
        self.save()
        if self.django_user.email != email:
            self.django_user.email = email
            self.django_user.save()


class Address(SantaBase):
    user = models.OneToOneField(SantaUser, related_name='address')
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    zipcode = models.CharField(max_length=32, null=True)

GiftTypes = (('RECIVIED', 'RECIVED'), ('SENT', 'SENT'))

class GiftingLog(SantaBase):
    user = models.ForeignKey(SantaUser, related_name='gifts')
    creation_time = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=32, choices=GiftTypes)

