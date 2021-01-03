
from django.urls import path
from . import views
urlpatterns = [
    path('category', views.create, name='category.course'),#localhost:8000/course/category
    path('read', views.read, name='read.course'),#localhost:8000/course/read
    path('update/<int:id>', views.update, name='update.course'),#localhost:8000/course/update/id
    path('delete/<int:id>', views.delete, name='delete.course'),#localhost:8000/course/delete/id
    path('dashboard', views.dashboard, name='dashboard.course'),  # localhost:8000/course/dashboard
]