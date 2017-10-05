from django.conf import settings
from django.shortcuts import render, redirect

from .models import Diary
from .forms import DiaryForm


def diary(request):
    if request.user.is_authenticated():
        return render(request, 'diary.html', {'diary_list': Diary.objects.all().filter(owner=request.user),
                                              'user_avatar': request.user.main_menu_avatar})
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))


def create_diary(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = DiaryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/diary/all/')
        else: # ==>GET method
            return render(request, 'create_diary.html', {'form': DiaryForm})
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))