
from django.urls import path
from category import views

urlpatterns = [
    path('category', views.create, name="create.category"), #localhost:8000/category/category
    path('read', views.read, name="read.category"), #localhost:8000/category/read
    path('dashboard', views.dashboard, name="dashboard.category"), #localhost:8000/category/dashboard
    path('update/<int:id>', views.update, name="update.category"), #localhost:8000/category/update
    path('delete/<int:id>', views.delete, name="delete.category"), #localhost:8000/category/delete
]

