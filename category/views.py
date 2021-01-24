from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED

from .serializers import CategorySerializer
from .forms import CategoryForm
from .models import Category
# Create your views here.


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


#==================================================
#===============================================api
#==================================================

@api_view(['POST'])
def api_create(request):
    if request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def api_read(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializers = CategorySerializer(categories, many=True)
        return Response(serializers.data)
    return Response("something went wrong!")


@api_view(['PUT'])
def api_update(request, id):
    if request.method == "PUT":
        category = Category.objects.get(id=id)
        serializer = CategorySerializer(category, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def api_delete(request, id):
    if request.method == "DELETE":
        category = Category.objects.get(id=id)
        category.delete()
        return Response("Deleted")