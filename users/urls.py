from django.contrib.auth.views import LoginView, LogoutView

from users.apps import UsersConfig
from django.urls import path

from users.views import UserCreateView, email_verification, ProfileView, recovery_password

app_name = UsersConfig.name

urlpatterns = [
    path("", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path('profile/', ProfileView.as_view(), name='profile'),
    path("recovery_password/", recovery_password, name="recovery"),
    path("email-confirm/<str:token>", email_verification, name="email-confirm"),
]
