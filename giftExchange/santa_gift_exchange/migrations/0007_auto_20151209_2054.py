# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('santa_gift_exchange', '0006_myuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='address',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='participate',
            name='sent',
            field=models.BooleanField(default=False),
        ),
    ]
