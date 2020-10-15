from django.urls import path

from . import views

app_name = "courses"

urlpatterns = [
    path("<str:subject_name>/", views.subject_view)
]
