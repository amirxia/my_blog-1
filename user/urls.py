
from django.urls import path, include
from . import views
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', views.register, name='register'),#localhost:8000/accounts/register
    path('profile/', views.profile, name='profile'),#localhost:8000/accounts/profile
    path('dashboard/', views.dashboard, name='dashboard'),#localhost:8000/accounts/dashboard
]
