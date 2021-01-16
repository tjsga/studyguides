from django.urls import path

from . import views

app_name = "courses"

urlpatterns = [
    path("subject/<str:subject_url>/", views.subject_view, name="subject_view"),
    path("tag/<str:tag>/", views.tag_view, name="tag"),
    path("course/<str:subject_url>/<str:course_url>/", views.course_view, name="course_view"),
    path("search/", views.search_view, name="search"),
    path("add/", views.add_view, name="add"),
    path("approve-index/", views.approve_index_view, name="approve_index_view"),
    path("approve/<int:request_id>/", views.approve_view, name="approve_view"),
]
