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
