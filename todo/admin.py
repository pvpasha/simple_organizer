from django.contrib import admin
from .models import *

class TaskOtherAdmin (admin.ModelAdmin):
    list_display = ('id', 'owner', 'title', 'creation_datetime', 'finishing_datetime', 'reminder',
                    'reminder_timedelta', 'percent')
    list_filter = ('owner', 'creation_datetime', 'finishing_datetime', 'reminder',
                   'percent')
    search_fields = ('owner', 'title', 'body')
    empty_value_display = '-empty-'
    readonly_field = ['id', ]

admin.site.register(TaskOther, TaskOtherAdmin)