from django.db import models


class SantaBase(models.Model):
    class Meta:
        abstract = True
        app_label = 'santa'


class User(SantaBase):
    django_user     = models.OneToOneField('auth.User', related_name='profile_entity', null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    playa_name = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    zipcode = models.CharField(max_length=32)
    willing_to_get = models.BinaryField(default=True)
    santa_to = models.ForeignKey('User', null=True)

    @property
    def email(self):
        return self.django_user.email


class GiftingLog(SantaBase):
    user = models.ForeignKey('User', related_name='gifts')
    creation_time = models.DateTimeField(auto_now_add=False)

