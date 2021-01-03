from django.shortcuts import render, redirect
from category.models import Category
from .forms import ArticleForm
from .models import Article

# Create your views here.


def create(request, id):
    category = Category.objects.get(id=id)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.category_id = category.id
            f.save()
            return redirect('dashboard')

    return render(request, 'admin/article/category.html', {'category': category})

def read(request, id):
    articles = Article.objects.filter(category_id=id)
    return render(request, 'admin/article/read.html', {'articles': articles})

def update(request, id):
    pass

def delete(request, id):
    pass
