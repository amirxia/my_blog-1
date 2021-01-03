from django.db import models
from category.models import Category

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50, null=False)
    body = models.TextField(null=False)
    image = models.ImageField(upload_to='static/article/images/')
    category =models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)