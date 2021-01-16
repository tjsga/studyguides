import random
import operator
from functools import reduce

from django import http
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from gdstorage.storage import GoogleDriveStorage
from django.core.exceptions import PermissionDenied

from .models import Subject, Course, Guide, Tag, Request
from .forms import StudyGuideRequestForm

gd_storage = GoogleDriveStorage()

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
            "subject_results": Subject.objects.filter(reduce(operator.or_, (Q(name__icontains=x) for x in q_list))),
            "course_results": [[c, c.subject.all()[0]] for c in Course.objects.filter(reduce(operator.or_, (Q(name__icontains=x) for x in q_list)))],
            "guide_results": Guide.objects.filter(reduce(operator.or_, (Q(name__icontains=x) for x in q_list))),
            "tag_results": Tag.objects.filter(reduce(operator.or_, (Q(name__icontains=x) for x in q_list))),
            "sq": q
        }
        return render(request, "search_results.html", context=context)

    return redirect(request.META["HTTP_REFERER"])

@login_required
def add_view(request):
    if request.method == "POST":
        form = StudyGuideRequestForm(request.POST, request.FILES)
        if form.is_valid():
            r = Request(name=form.cleaned_data["name"])
            r.save()
            r.course.add(form.cleaned_data["course"])
            for t in form.cleaned_data["tags"]:
                r.tags.add(t)
            r.guide = form.cleaned_data["guide"]
            r.save()
            return redirect(reverse("home:index"))
        return render(request, "add.html", context={"form": form})
    else:
        form = StudyGuideRequestForm()
        return render(request, "add.html", context={"form": form})

@login_required
def approve_index_view(request):
    if request.user.is_superuser or request.user.is_staff:
        return render(request, "approve_index.html", context={"guide_requests": Request.objects.all()})
    raise PermissionDenied

@login_required
def approve_view(request, request_id):
    if request.user.is_superuser or request.user.is_staff:
        guide_request = Request.objects.get(id=request_id)
        if request.method == "POST":
            if request.POST.get("approve"):
                guide = Guide(name=guide_request.name)
                guide.save()
                for t in guide_request.tags.all():
                    guide.tags.add(t)
                guide.course = guide_request.course.all()[0]
                guide.url = guide_request.guide.url
                guide.save()
            guide_request.delete()
            return redirect(reverse("courses:approve_index_view"))
        else:
            ctx = {
                "guide_request": guide_request,
                "course": guide_request.course.all()[0],
                "tags": guide_request.tags.all()
            }
            return render(request, "approve.html", context=ctx)
    raise PermissionDenied
