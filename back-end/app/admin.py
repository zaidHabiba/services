from django.contrib import admin
from app.models import *
from django.contrib.auth.models import Permission, Group


admin.site.register(Country)
admin.site.register(Image)
admin.site.register(ChangeLog)
admin.site.register(User)
admin.site.register(Permission)
