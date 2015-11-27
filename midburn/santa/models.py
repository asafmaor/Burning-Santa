from django.db import models

class SantaBase(models.Model):
    class Meta:
        abstract = True
        app_label = 'santa'


class User(SantaBase):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    playa_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    zipcode = models.CharField(max_length=32)
    santa = models.ForeignKey('User')
