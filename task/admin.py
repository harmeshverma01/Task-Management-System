from django.contrib import admin

from task.models import CreateUser, Task

# Register your models here.

admin.site.register(Task)
admin.site.register(CreateUser)

