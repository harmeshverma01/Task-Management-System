from django.urls import path

from .views import *

urlpatterns = [
    path('assign-task', TaskView.as_view()),
    path('task_status', TaskStatusView.as_view()),
    path('check_status', CheckTaskView.as_view()),
    path('managercheckstatus', ManagerCheckTaskView.as_view()),
    path('managertask', ManagertoManagerView.as_view())
]
