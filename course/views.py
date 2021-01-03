from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CourseForm
# Create your views here.
from .models import Course


@login_required
def create(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('read.dashboard')

    return render(request, 'course/create.html')

def read(request):
    courses = Course.objects.all()
    return render(request, 'course/read.html', {'courses': courses})


@login_required
def update(request, id):
    course = Course.objects.get(id=id)
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('read.dashboard')
    return render(request, 'course/update.html', {'course': course})

@login_required
def delete(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('read.dashboard')

@login_required
def dashboard(request):
    courses = Course.objects.all()
    return render(request, 'course.html', {'courses': courses})
