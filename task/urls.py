from django.urls import path

from .views import *

urlpatterns = [
    path('assign-task', TaskView.as_view()),
    path('task_status', TaskStatusView.as_view()),
    path('check_status', CheckTaskView.as_view()),
    path('userstatus', UserstatusView.as_view())
]
