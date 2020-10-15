import random

from django import http
from django.shortcuts import render, redirect, reverse, get_object_or_404

from .models import Subject, Course, Guide


def subject_view(request, subject_url):
    subject = get_object_or_404(Subject, url=subject_url)
    return render(request, "subject.html", {"subject": subject,
                                            "courses": subject.courses.all()})


def course_view(request, subject_url, course_url):
    subject = get_object_or_404(Subject, url=subject_url)
    course = get_object_or_404(Course, url=course_url)
    return render(request, "course.html", {"subject": subject,
                                           "course": course,
                                           "guides": Guide.objects.filter(course=course)})
