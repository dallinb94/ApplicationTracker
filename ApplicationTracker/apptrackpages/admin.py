from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Application, User

# Register your models here.
admin.site.register(Application)
admin.site.register(User,UserAdmin)
