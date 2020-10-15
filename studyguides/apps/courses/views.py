import random

from django import http
from django.shortcuts import render, redirect, reverse, get_object_or_404

from .models import Subject, Course, Guide


def subject_view(request, subject_name):
    print(subject_name)
    subject = get_object_or_404(Subject, url=subject_name)
    return render(request, "subject.html", {"subject": subject, "courses": subject.courses.all()})
