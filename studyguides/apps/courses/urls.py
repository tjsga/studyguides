from django.urls import path

from . import views

app_name = "courses"

urlpatterns = [
    path("subject/<str:subject_url>/", views.subject_view),
    path("tag/<str:tag>/", views.tag_view, name="tag"),
    path("course/<str:subject_url>/<str:course_url>/", views.course_view),
]
