from django import forms

from .models import PasswordOrganizer


class PasswordOrganizerForm(forms.ModelForm):

    class Meta:
        model = PasswordOrganizer
        fields = ('owner', 'resource_url', 'password_res')