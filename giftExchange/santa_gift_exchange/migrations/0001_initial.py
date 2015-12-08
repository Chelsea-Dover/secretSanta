# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('revival_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User profiles',
            },
        ),
        migrations.CreateModel(
            name='Participate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('getting', models.ForeignKey(to='santa_gift_exchange.Participate', related_name='gettinggift')),
                ('giveruser', models.ForeignKey(to='santa_gift_exchange.MyUser')),
                ('giving', models.ForeignKey(to='santa_gift_exchange.Participate', related_name='givinggift')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='elf',
            field=models.ManyToManyField(to='santa_gift_exchange.Participate'),
        ),
    ]
