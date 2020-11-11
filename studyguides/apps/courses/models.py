from django.db import models
from django.core.validators import RegexValidator, FileExtensionValidator


class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    url = models.CharField("URL", max_length=20, unique=True, validators=[RegexValidator(
        regex="^[a-zA-Z0-9_\-]+$", message="Only alphanumeric, dashes, and underscores allowed")])

    courses = models.ManyToManyField("Course", related_name="subject")

    def __str__(self):
        return self.name


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    url = models.CharField("URL", max_length=20, unique=True, validators=[RegexValidator(
        regex="^[a-zA-Z0-9_\-]+$", message="Only alphanumeric, dashes, and underscores allowed")])

    def __str__(self):
        return self.name


class Guide(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    tags = models.ManyToManyField("Tag", related_name="guide")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    url = models.URLField(max_length=300)

    def __str__(self):
        return self.name

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    url = models.SlugField(max_length=100, unique=True, null=True, validators=[RegexValidator(
        regex="^[a-z0-9_\-]+$", message="Only lowercase alphanumeric, dashes, and underscores allowed")])

    class Meta:
        ordering = ['url']

    def __str__(self):
        return self.name