from django import forms

from .models import ShortTask, Task, Event


class ShortTaskForm(forms.ModelForm):

    class Meta:
        model = ShortTask
        fields = ('owner', 'title', 'body', 'category', 'creation_date', 'finished')


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('owner', 'title', 'body', 'category', 'creation_date', 'finishing_date', 'finished', 'reminder')


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('owner', 'title', 'body', 'category', 'creation_date', 'finished', 'event_date')