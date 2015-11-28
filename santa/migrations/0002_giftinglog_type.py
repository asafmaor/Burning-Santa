# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('santa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='giftinglog',
            name='type',
            field=models.CharField(default='SENT', max_length=32, choices=[(b'RECIVIED', b'RECIVED'), (b'SENT', b'SENT')]),
            preserve_default=False,
        ),
    ]
