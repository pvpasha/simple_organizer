from django.conf import settings
from django.shortcuts import render, redirect

from contacts.models import *


def contacts(request):
    if request.user.is_authenticated():
        return render(request, 'contacts.html', {'contact_list': Contact.objects.all().filter(owner=request.user),
                                               'user_avatar': request.user.main_menu_avatar})
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))

