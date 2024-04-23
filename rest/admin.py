from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(Board)
admin.site.register(Cell)
admin.site.register(GameUser, UserAdmin)
# Register your models here.
