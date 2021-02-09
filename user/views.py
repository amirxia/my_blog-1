from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect

from course.models import Course

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
    permission = Permission.objects.get(
        codename='add_course',
        content_type=content_type,
    )
    user.user_permissions.add(permission)

    return redirect('login')