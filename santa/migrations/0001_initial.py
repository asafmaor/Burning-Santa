# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=1000)),
                ('zipcode', models.CharField(max_length=32, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GiftingLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(max_length=100, null=True)),
                ('type', models.CharField(max_length=32, choices=[(b'RECIVIED', b'RECIVED'), (b'SENT', b'SENT')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SantaUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('_email', models.EmailField(max_length=254, db_column=b'email')),
                ('is_signed_in', models.BinaryField(default=False)),
                ('playa_name', models.CharField(max_length=100, null=True)),
                ('willing_to_get', models.BinaryField(default=True)),
                ('what_makes_you_happy', models.CharField(max_length=100, null=True)),
                ('what_makes_you_sad', models.CharField(max_length=100, null=True)),
                ('what_power_ranger_are_you', models.CharField(max_length=100, null=True)),
                ('django_user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('santa_to', models.ForeignKey(to='santa.SantaUser', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='giftinglog',
            name='user',
            field=models.ForeignKey(related_name='gifts', to='santa.SantaUser'),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.OneToOneField(related_name='address', to='santa.SantaUser'),
        ),
    ]
