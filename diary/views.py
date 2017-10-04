from django.conf import settings
from django.shortcuts import render, redirect

from diary.models import Diary


def diary(request):
    if request.user.is_authenticated():
        return render(request, 'diary.html', {'diary_list': Diary.objects.all().filter(owner=request.user),
                                              'user_avatar': request.user.main_menu_avatar})
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))