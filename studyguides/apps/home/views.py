from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.apps import apps
from django.contrib.auth.decorators import login_required

Subject = apps.get_model("courses", "Subject")
Course = apps.get_model("courses", "Course")

@login_required
def index_view(request):
    return render(request, "home.html", {"subjects": [(subject, Course.objects.filter(subject=subject)) for subject in Subject.objects.all()]})
