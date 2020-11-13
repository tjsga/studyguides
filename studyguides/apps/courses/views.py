import random
import operator
from functools import reduce

from django import http
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Subject, Course, Guide, Tag

@login_required
def subject_view(request, subject_url):
    subject = get_object_or_404(Subject, url=subject_url)
    return render(request, "subject.html", {"subject": subject,
                                            "courses": subject.courses.all().order_by("name")})

@login_required
def course_view(request, subject_url, course_url):
    subject = get_object_or_404(Subject, url=subject_url)
    course = get_object_or_404(Course, url=course_url)
    return render(request, "course.html", {"subject": subject,
                                           "course": course,
                                           "guides": [[g, g.tags.all()] for g in Guide.objects.filter(course=course).order_by("name")]})

@login_required
def tag_view(request, tag):
    tag = get_object_or_404(Tag, name=tag)
    return render(request, "tag.html", {"tag": tag, "guides": [[g, g.tags.all()] for g in tag.guide.all().order_by("name")]})

@login_required
def search_view(request):
    q = request.GET.get("q", "").strip()

    if q:
        q_list = q.split()
        context = {
            "subject_results": Subject.objects.filter(reduce(operator.or_, (Q(name__contains=x) for x in q_list))),
            "course_results": [[c, c.subject.all()[0]] for c in Course.objects.filter(reduce(operator.or_, (Q(name__contains=x) for x in q_list)))],
            "guide_results": Guide.objects.filter(reduce(operator.or_, (Q(name__contains=x) for x in q_list))),
            "tag_results": Tag.objects.filter(reduce(operator.or_, (Q(name__contains=x) for x in q_list))),
            "sq": q
        }
        return render(request, 'search_results.html', context=context)

    return redirect(request.META["HTTP_REFERER"])
