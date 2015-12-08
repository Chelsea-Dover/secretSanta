# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('santa_gift_exchange', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participate',
            name='getting',
            field=models.ForeignKey(to='santa_gift_exchange.Participate', related_name='gettinggift', blank=True),
        ),
        migrations.AlterField(
            model_name='participate',
            name='giving',
            field=models.ForeignKey(to='santa_gift_exchange.Participate', related_name='givinggift', blank=True),
        ),
    ]
