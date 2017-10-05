from django.conf import settings
from django.shortcuts import render, redirect

from .models import PasswordOrganizer
from .forms import PasswordOrganizerForm


def passorg(request):
    if request.user.is_authenticated():
        return render (request, 'passorg.html', {'pass_list': PasswordOrganizer.objects.all().filter(
            owner=request.user), 'user_avatar': request.user.main_menu_avatar})
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))


def create_passw(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = PasswordOrganizerForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/passorg/all/')
        else: # ==>GET method
            return render(request, 'create_passw.html', {'form': PasswordOrganizerForm})
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))