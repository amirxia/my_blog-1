

from django.urls import path
from . import views
urlpatterns = [
    path('create/<int:id>', views.create, name="create.article"), #localhost:8000/article/create
    path('read/<int:id>', views.read, name="read.article"), #localhost:8000/article/read
    path('update/<int:id>', views.update, name="update.article"), #localhost:8000/article/update
    path('delete/<int:id>', views.delete, name="delete.article"), #localhost:8000/article/delete

    path('api-read', views.api_read),
]