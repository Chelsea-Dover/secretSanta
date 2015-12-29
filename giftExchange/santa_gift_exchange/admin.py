from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Participate)
admin.site.register(Group)