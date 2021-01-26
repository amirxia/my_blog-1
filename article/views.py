from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from category.models import Category
from .forms import ArticleForm
from .models import Article

# Create your views here.
from .serializers import ArticleSerializer


def create(request, id):
    category = Category.objects.get(id=id)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.category_id = category.id
            f.save()
            return redirect('dashboard.category')

    return render(request, 'create_article.html', {'category': category})

def read(request, id):
    articles = Article.objects.filter(category_id=id)
    category = Category.objects.get(id=id)
    return render(request, 'article.html', {'articles': articles, 'category': category})

def update(request, id):
    pass

def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('dashboard.category')


@api_view(['POST'])
def api_create(request, category_id):

    category = Category.objects.get(id=category_id)

    if request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(category_id=category.id)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def api_read(request, category_id):
    if request.method == "GET":
        article = Article.objects.filter(category_id=category_id)
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)


@api_view(['PUT'])
def api_update(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == "PUT":
        serializer = ArticleSerializer(article, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def api_delete(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == "DELETE":
        article.delete()
        return Response("DELETED")

