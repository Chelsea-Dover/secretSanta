# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('santa_gift_exchange', '0004_auto_20151203_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participate',
            name='giveruser',
            field=models.ForeignKey(related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
