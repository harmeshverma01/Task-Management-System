from django.urls import path

from task.views import  CheckCompletedtaskView,  TaskView, TaskStatusView

urlpatterns = [
    path('Assign-task', TaskView.as_view()),
    path('completed-task', CheckCompletedtaskView.as_view()),
    path('task_status', TaskStatusView.as_view()),
]
