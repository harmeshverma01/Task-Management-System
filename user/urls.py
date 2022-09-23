from django.urls import path
from .views import Loginview, ManagerView, UserdetailsView, Userview


urlpatterns = [
    path('users', Userview.as_view()),
    path('login', Loginview.as_view()),
    path('user_details', UserdetailsView.as_view()),
    path('manager', ManagerView.as_view())
]
