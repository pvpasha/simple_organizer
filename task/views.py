from django.conf import settings
from django.shortcuts import render, redirect
from task.models import *
#from todo.views import template


def task(request):
    if request.user.is_authenticated():
        return render(request, 'task.html', {'short_task_list': ShortTask.objects.all().filter(owner=request.user),
                                            'task_list': Task.objects.all().filter(owner=request.user),
                                            'event_list': Event.objects.all().filter(owner=request.user),
                                             'user_avatar': request.user.main_menu_avatar})
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))

