# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
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
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SantaUser',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('playa_name', models.CharField(max_length=100, null=True)),
                ('willing_to_get', models.BinaryField(default=True)),
                ('santa_to', models.ForeignKey(to='santa.SantaUser', null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='giftinglog',
            name='user',
            field=models.ForeignKey(related_name='gifts', to='santa.SantaUser'),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(related_name='address', to='santa.SantaUser'),
        ),
    ]
