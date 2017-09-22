from django.contrib import admin
from .models import *


class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'finished')
    list_filter = ('id', 'owner')
    search_fields = ('id', 'title', 'owner', 'finished')
    empty_value_display = '-empty-'
    readonly_field = ['id',]

class TaskAdmin (admin.ModelAdmin):
    list_display = ('id', 'owner', 'title', 'creation_datetime', 'finishing_datetime', 'reminder',
                    'reminder_timedelta', 'percent', 'category')
    list_filter = ('owner', 'creation_datetime', 'finishing_datetime', 'reminder',
                   'percent', 'category')
    search_fields = ('owner', 'title', 'body')

class EventAdmin (admin.ModelAdmin):
    list_display = ('id', 'owner', 'title', 'category', 'event_datetime', 'repeat')
    list_filter = ('owner', 'title', 'category', 'event_datetime', 'repeat')
    search_fields = ('owner', 'title')

class DiaryAdmin (admin.ModelAdmin):
    list_display = ('id', 'owner', 'title', 'creation_date')
    list_filter = ('owner', 'creation_date')
    search_fields = ('owner', 'title')

class BudgetAdmin (admin.ModelAdmin):
    list_display = ('id', 'owner', 'cash', 'income', 'outcome')

class ContactAdmin (admin.ModelAdmin):
    list_display = ('id', 'phone', 'name', 'forename', 'birthday', 'add_reminder')
    list_filter = ('phone', 'name', 'forename')
    search_fields = ('phone', 'name', 'forename')

class PasswordOrganizerAdmin (admin.ModelAdmin):
    pass


admin.site.register(ToDo, ToDoAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Diary, DiaryAdmin)
admin.site.register(Budget, BudgetAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(PasswordOrganizer, PasswordOrganizerAdmin)