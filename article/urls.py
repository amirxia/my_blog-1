

from django.urls import path
from . import views
urlpatterns = [
    path('create/<int:id>', views.create, name="create.article"), #localhost:8000/article/create
    path('read/<int:id>', views.read, name="read.article"), #localhost:8000/article/read
    path('update/<int:id>', views.update, name="update.article"), #localhost:8000/article/update
    path('delete/<int:id>', views.delete, name="delete.article"), #localhost:8000/article/delete


    path('api/v1/create/<int:category_id>', views.api_create, name='api.create.article'), #localhost:8000/article/api/v1/create/id
    path('api/v1/read/<int:category_id>', views.api_read, name='api.read.article'), #localhost:8000/article/api/v1/read/id
    path('api/v1/update/<int:article_id>', views.api_update, name='api.update.article'), #localhost:8000/article/api/v1/update/id
    path('api/v1/delete/<int:article_id>', views.api_delete, name='api.delete.article'), #localhost:8000/article/api/v1/delete/id

]