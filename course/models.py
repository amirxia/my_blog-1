from django.db import models

# Create your models here.



class Course(models.Model):
    title = models.CharField(max_length=50, null=False)
    body = models.TextField()
    price = models.CharField(max_length=20, null=False)
    image = models.ImageField(upload_to='static/course/images/')
    creator = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)