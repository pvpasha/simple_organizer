from django.conf import settings
from django.shortcuts import render, render_to_response, redirect

from .models import ShortTask, Task, Event
from .forms import ShortTaskForm, TaskForm, EventForm


def task(request):
    if request.user.is_authenticated():
        return render(request, 'task.html', {'short_task_list': ShortTask.objects.all().filter(owner=request.user),
                                            'task_list': Task.objects.all().filter(owner=request.user),
                                            'event_list': Event.objects.all().filter(owner=request.user),
                                             'user_avatar': request.user.main_menu_avatar})
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))

# def owner(request):
#     return request.user

def create_short_task(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = ShortTaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/task/all/')
        else: # ==>GET method
            return render(request, 'createShortTask.html', {'form': ShortTaskForm})
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))


def create_task(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/task/all/')
        else: # ==>GET method
            return render(request, 'createTask.html', {'form': TaskForm})
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))


def create_event(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = EventForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/task/all/')
        else: # ==>GET method
            return render(request, 'createEvent.html', {'form': EventForm})
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))