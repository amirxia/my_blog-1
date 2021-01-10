from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import CategoryForm
from .models import Category
# Create your views here.
from .serializers import CategorySerializer


def create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard.category')

    return render(request, 'category/create.html')

def read(request):
    categories = Category.objects.all()
    return render(request, '', {'categories': categories})

def dashboard(request):
    categories = Category.objects.all()
    return render(request, 'category/category.html', {'categories': categories})

def update(request, id):
    pass

def delete(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('dashboard.category')


@api_view(['get'])
def api_read(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
