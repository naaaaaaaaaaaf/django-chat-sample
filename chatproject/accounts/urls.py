from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import AccountRegisterView

urlpatterns = [
    path('register/', AccountRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
]
