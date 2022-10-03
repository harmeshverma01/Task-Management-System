from django.contrib import admin

from task.models import  Task

# Register your models here.



@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "id", "user_id", "manager_id", "status"
    ]
    


