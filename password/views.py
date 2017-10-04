from django.conf import settings
from django.shortcuts import render, redirect

from password.models import PasswordOrganizer


def passorg(request):
    if request.user.is_authenticated():
        return render (request, 'passorg.html', {'pass_list': PasswordOrganizer.objects.all().filter(
            owner=request.user), 'user_avatar': request.user.main_menu_avatar})
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))