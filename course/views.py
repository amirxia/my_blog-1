from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from .forms import CourseForm
# Create your views here.
from .models import Course
from .serializers import CourseSerializer


@login_required
@permission_required('course.add_course')
def create(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard.course')

    return render(request, 'create.html')

def read(request):
    courses = Course.objects.all()
    return render(request, 'course/read.html', {'courses': courses})


@login_required
def update(request, id):

    if request.user.has_perm("course.change_course"):
        course = Course.objects.get(id=id)
        if request.method == "POST":
            form = CourseForm(request.POST, request.FILES, instance=course)
            if form.is_valid():
                form.save()
                return redirect('read.dashboard')
    else:
        return redirect('register')
    return render(request, 'course/update.html', {'course': course})

@login_required
def delete(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('dashboard.course')

@login_required

def dashboard(request):
    courses = Course.objects.all()
    return render(request, 'course.html', {'courses': courses})


@api_view(['POST'])
def api_create(request):
    if request.method == "POST":
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

