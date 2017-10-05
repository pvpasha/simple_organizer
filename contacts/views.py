from django.conf import settings
from django.shortcuts import render, redirect

from .models import Contact
from .forms import ContactForm


def contacts(request):
    if request.user.is_authenticated():
        return render(request, 'contacts.html', {'contact_list': Contact.objects.all().filter(owner=request.user),
                                               'user_avatar': request.user.main_menu_avatar})
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))


def create_contact(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/contacts/all/')
        else: # ==>GET method
            return render(request, 'create_contact.html', {'form': ContactForm})
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))