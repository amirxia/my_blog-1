
from django.urls import path
from . import views
urlpatterns = [
    path('create', views.create, name='course.create'),#localhost:8000/course/create
    path('read', views.read, name='read.course'),#localhost:8000/course/read
    path('update/<int:id>', views.update, name='update.course'),#localhost:8000/course/update/id
    path('delete/<int:id>', views.delete, name='delete.course'),#localhost:8000/course/delete/id
    path('dashboard', views.dashboard, name='dashboard.course'),  # localhost:8000/course/dashboard

    path('api/v1/create', views.api_create, name="api.create.course")


]