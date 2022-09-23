from django.urls import path
from .views import AssignUserView, Loginview, ManagerView, RegisterView, UserdetailsView, Userview


urlpatterns = [
    path('users', Userview.as_view()),
    path('login', Loginview.as_view()),
    path('user_details', UserdetailsView.as_view()),
    path('manager', ManagerView.as_view()),
    path('admin-assign', AssignUserView.as_view()),
    path('register', RegisterView.as_view())
]
