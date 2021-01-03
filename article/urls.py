

from django.urls import path
from . import views
urlpatterns = [
    path('category/<int:id>', views.create, name="category.article"), #localhost:8000/article/category
    path('read/<int:id>', views.read, name="read.article"), #localhost:8000/article/read
    path('update/<int:id>', views.update, name="update.article"), #localhost:8000/article/update
    path('delete/<int:id>', views.delete, name="delete.article"), #localhost:8000/article/delete
]