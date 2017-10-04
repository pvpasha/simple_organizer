from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect

from budget.models import *


def budget(request):
    #html = '<h1 style="color: red;">You have %d invoice(s)</h1>' % len(Invoice.objects.all().filter(owner=request.user))
    if request.user.is_authenticated():
    #    return HttpResponse(html, status=200)
        return render(request, 'budget.html', {'invoice_list': Invoice.objects.all().filter(owner=request.user),
                                               'user_avatar': request.user.main_menu_avatar})
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))

