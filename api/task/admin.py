from django.contrib import admin
from .models import CategoryTask, ShortTask, Task, Event


class CategoryTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner')
    list_filter = ('owner',)
    search_fields = ('id', 'title')
    empty_value_display = '-empty-'
    readonly_field = ['id', ]


class ShortTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'finished')
    list_filter = ('finished',)
    search_fields = ('id', 'title')
    empty_value_display = '-empty-'
    readonly_field = ['id', ]


class TaskAdmin (admin.ModelAdmin):
    list_display = ('id', 'owner', 'title', 'creation_date', 'finishing_date', 'category')
    list_filter = ('owner', 'category', 'finished')
    search_fields = ('id', 'title')


class EventAdmin (admin.ModelAdmin):
    list_display = ('id', 'owner', 'title', )
    list_filter = ('owner',)
    search_fields = ('id', 'owner', 'title')


admin.site.register(CategoryTask, CategoryTaskAdmin)
admin.site.register(ShortTask, ShortTaskAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Event, EventAdmin)
