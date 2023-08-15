from django.urls import path
from .views import *

urlpatterns = [
    path("", Register, name="signup"),
    path("login", loginView, name="login"),
    path("logout", logoutView, name="logout"),
    path("profile", profile, name="profile"),
]
