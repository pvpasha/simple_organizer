from django.contrib import admin

from .models import ToDo


class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'finished')
    list_filter = ('id', 'owner', 'finished')
    search_fields = ('id', 'title', 'owner', 'finished')
    empty_value_display = '-empty-'
    readonly_field = ['id',]


admin.site.register(ToDo, ToDoAdmin)