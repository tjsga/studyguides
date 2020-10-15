from django.urls import path

from . import views

app_name = "courses"

urlpatterns = [
    path("<str:subject_url>/", views.subject_view),
    path("<str:subject_url>/<str:course_url>/", views.course_view),
]
