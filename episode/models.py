from django.db import models

# Create your models here.
from course.models import Course


class Episode(models.Model):

    title = models.CharField(max_length=50, null=False)
    time = models.CharField(max_length=10, null=False)
    video = models.FileField(upload_to='static/episode/videos/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
