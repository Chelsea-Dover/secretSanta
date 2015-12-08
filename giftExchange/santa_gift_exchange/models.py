from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
# s

# class People(models.Model):


# class MyUser(models.Model):
#     user = models.OneToOneField(User)
#
#     def __str__(self):
#         return self.user.username
#
#     class Meta:
#         verbose_name_plural = u'User profiles'


class Participate(models.Model):
    giving = models.ForeignKey('self', related_name="givinggift", null=True, blank=True)
    getting = models.ForeignKey('self', related_name="gettinggift", null=True, blank=True)
    giveruser = models.ForeignKey(User, related_name='user')


class Group(models.Model):
    group_name = models.CharField(max_length=120, default=None)
    elf = models.ManyToManyField(Participate)
    revival_date = models.DateTimeField(auto_now_add=True)

    def save(self):
        from datetime import timedelta
        d = timedelta(days=60)

        # only add 60 days if it's the first time the model is saved
        if not self.id:
            # not saving the model before adding the timedelta gave me errors
            super(Group, self).save()

            self.revival_date += d

            # final save
            super(Group, self).save()

