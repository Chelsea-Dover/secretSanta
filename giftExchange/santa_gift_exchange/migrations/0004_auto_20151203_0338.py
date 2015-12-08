# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('santa_gift_exchange', '0003_auto_20151203_0327'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_name',
            field=models.CharField(default=None, max_length=120),
        ),
        migrations.AlterField(
            model_name='participate',
            name='getting',
            field=models.ForeignKey(related_name='gettinggift', blank=True, null=True, to='santa_gift_exchange.Participate'),
        ),
        migrations.AlterField(
            model_name='participate',
            name='giving',
            field=models.ForeignKey(related_name='givinggift', blank=True, null=True, to='santa_gift_exchange.Participate'),
        ),
    ]
