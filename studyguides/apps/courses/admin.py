from django.contrib import admin
from .models import Subject, Course, Guide, Tag, Request
# Register your models here.

admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Guide)
admin.site.register(Tag)
admin.site.register(Request)
