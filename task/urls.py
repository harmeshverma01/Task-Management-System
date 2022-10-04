from django.urls import path

from .views import *

urlpatterns = [
    path('assign-task', TaskView.as_view()),
    path('task_status', TaskStatusView.as_view()),
    path('check_status', CheckTaskView.as_view()),
    path('managercheckstatus', ManagerCheckTaskView.as_view()),
    path('managertask', ManagertoManagerView.as_view()),
    path('taskcomplete/<int:id>', TaskCompleteView.as_view()),
    path('taskcomplete', TaskCompleteView.as_view()),
    path('taskrating', TaskRatingView.as_view()),
    path('taskrating/<int:id>', TaskRatingView.as_view()),
    path('check_rating', UserCheckTaskRatingView.as_view()), 
    path('managercheckrating', ManagerCheckTasKRatingView.as_view())
]