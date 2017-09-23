from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner')
    list_filter = ('owner',)
    search_fields = ('id', 'title', 'owner')
    empty_value_display = '-empty-'
    readonly_field = ['id', ]


class ShortTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'creation_date', 'category', 'finished')
    list_filter = ('owner', 'category')
    search_fields = ('id', 'title', 'owner')
    empty_value_display = '-empty-'
    readonly_field = ['id',]


class TaskAdmin (admin.ModelAdmin):
    list_display = ('id', 'owner', 'title', 'creation_date', 'finishing_date', 'category')
    list_filter = ('owner', 'category')
    search_fields = ('id', 'owner', 'title')


class EventAdmin (admin.ModelAdmin):
    list_display = ('id', 'owner', 'title', 'category')
    list_filter = ('owner', 'category')
    search_fields = ('id', 'owner', 'title')

admin.site.register(Category, CategoryAdmin)
admin.site.register(ShortTask, ShortTaskAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Event, EventAdmin)