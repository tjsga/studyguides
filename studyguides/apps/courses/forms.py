from django import forms

from .models import Request, Course, Tag

class StudyGuideRequestForm(forms.Form):
    name = forms.CharField(max_length=100)
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)
    guide = forms.FileField()
