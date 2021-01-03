from django.shortcuts import render, redirect

# Create your views here.
from course.models import Course
from episode.forms import EpisodeForm
from episode.models import Episode


def create(request, id):
    course = Course.objects.get(id=id)
    if request.method == "POST":
        form = EpisodeForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.course_id = id
            f.save()
            return redirect('dashboard')

    return render(request, 'episode/create.html', {'course': course})

def read(request, id):
    episodes = Episode.objects.filter(course_id=id)
    course = Course.objects.get(id=id)
    return render(request, 'admin/episode.html', {'episodes': episodes, 'course': course})

def update(request, id):
    episode = Episode.objects.get(id=id)
    if request.method == "POST":
        form = EpisodeForm(request.POST, request.FILES, instance=episode)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    return render(request, 'episode/update.html', {'episode': episode})


def delete(request, id):
    episode = Episode.objects.get(id=id)
    episode.delete()
    return redirect('dashboard')
