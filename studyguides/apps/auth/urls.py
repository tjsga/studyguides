from django.urls import path

from . import views

app_name = "auth"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout_view, name="logout"),
]

