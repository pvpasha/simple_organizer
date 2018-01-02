from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('owner', 'name', 'surname', 'phone', 'birthday', 'add_reminder')