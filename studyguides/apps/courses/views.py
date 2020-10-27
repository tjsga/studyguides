import random

from django import http
from django.shortcuts import render, redirect, reverse, get_object_or_404

from .models import Subject, Course, Guide, Tag


def subject_view(request, subject_url):
    subject = get_object_or_404(Subject, url=subject_url)
    return render(request, "subject.html", {"subject": subject,
                                            "courses": subject.courses.all()})


def course_view(request, subject_url, course_url):
    subject = get_object_or_404(Subject, url=subject_url)
    course = get_object_or_404(Course, url=course_url)
    return render(request, "course.html", {"subject": subject,
                                           "course": course,
                                           "guides": [[g, g.tags.all()] for g in Guide.objects.filter(course=course)]})

def tag_view(request, tag):
    tag = get_object_or_404(Tag, name=tag)
    return render(request, "tag.html", {"tag": tag, "guides": [[g, g.tags.all()] for g in tag.guide.all()]})