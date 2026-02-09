from django.contrib import admin

from app1.models import Task


# Register your models here.
class Admin(admin.ModelAdmin):
    pass
admin.site.register(Task, Admin)