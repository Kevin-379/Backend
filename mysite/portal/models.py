from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class ProfessorReview(models.Model):
    name = models.CharField(max_length=20)
    comments = models.TextField()
    time = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.SET('[Deleted]'))
    courses_taught = models.CharField(max_length=50, blank=True)
    rating = models.IntegerField()
    difficulty = models.CharField(max_length=20, blank=True)
    changed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('prof_review_detail', kwargs={'pk': self.pk})


class CourseReview(models.Model):
    code = models.CharField(max_length=6)
    comments = models.TextField()
    time = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.SET('[Deleted]'))
    rating = models.IntegerField()
    difficulty = models.CharField(max_length=20)
    taught_by = models.CharField(max_length=20)
    requirements = models.CharField(max_length=20, blank=True)
    recommended_for = models.TextField(blank=True)
    changed = models.BooleanField(default=False)

    def __str__(self):
        return self.code

    def get_absolute_url(self):
        return reverse('course_review_detail', kwargs={'pk': self.pk})


class Professor(models.Model):
    name = models.CharField(max_length=20)
    courses_taught = models.TextField()
    rating = models.FloatField()
    total = models.PositiveIntegerField(default=1)

    @classmethod
    def create(cls, name, courses_taught, rating):
        prof = Professor(name=name, courses_taught=courses_taught, rating=rating, total=1)
        prof.save()
        return prof


class Course(models.Model):
    code = models.CharField(max_length=6)
    rating = models.FloatField()
    total = models.PositiveIntegerField(default=1)

    @classmethod
    def create(cls, code, rating):
        course = cls(code=code, rating=rating, total=1)
        return course
