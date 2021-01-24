
from django.urls import path
from category import views

urlpatterns = [
    path('create', views.create, name="create.create"), #localhost:8000/create/category
    path('read', views.read, name="read.category"), #localhost:8000/category/read
    path('dashboard', views.dashboard, name="dashboard.category"), #localhost:8000/category/dashboard
    path('update/<int:id>', views.update, name="update.category"), #localhost:8000/category/update
    path('delete/<int:id>', views.delete, name="delete.category"), #localhost:8000/category/delete

    path('api/v1/create', views.api_create, name="api.create.category"),
    path('api/v1/read', views.api_read, name="api.read.category"),
    path('api/v1/update/<int:id>', views.api_update, name="api.update.category"),
    path('api/v1/delete/<int:id>', views.api_delete, name="api.delete.category"),
]

