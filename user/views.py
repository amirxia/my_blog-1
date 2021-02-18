from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission, User, Group
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect

from course.models import Course
from episode.models import Episode
from category.models import Category
from article.models import Article


# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def perm(request, id):

    user = User.objects.get(id=id)

    content_type = ContentType.objects.get_for_model(Course)
    permission_add = Permission.objects.get(codename='add_course',content_type=content_type)
    permission_change = Permission.objects.get(codename='change_course',content_type=content_type)

    user.user_permissions.add(permission_add, permission_change)

    return redirect('login')

def manage_user(request):

    if request.method == "POST":

        new_group, created = Group.objects.get_or_create(name=request.POST['group_name'])
        ct = ContentType.objects.get_for_model(eval(request.POST['choose']))
        new_perm, created_perm = Permission.objects.get_or_create(
            codename=request.POST['perm_code'],
            name=request.POST['perm_name'],
            content_type=ct
        )

        if new_group:
            if new_perm:
                new_group.permissions.add(new_perm)

    models = [model.__name__ for model in apps.get_models()]
    return render(request, 'manage.html', {'models': models})

