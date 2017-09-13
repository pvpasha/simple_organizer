from django import forms
from django.contrib.auth.forms import (ReadOnlyPasswordHashField,
                                       UserCreationForm as _UserCreationForm,
                                       UserChangeForm as _UserChangeForm)
#from PIL

from .models import OrganizerUser


class UserCreationForm(_UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = OrganizerUser
        fields = ('user_mail', 'password1', 'password2', 'first_name', 'second_name', 'avatar')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(_UserChangeForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = OrganizerUser
        fields = '__all__'

    def clean_password(self):
        return self.initial["password"]