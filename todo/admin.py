from django.contrib import admin

from .models import ToDo, Task, Contact


class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'finished')
    list_filter = ('id', 'owner')
    search_fields = ('id', 'title', 'owner', 'finished')
    empty_value_display = '-empty-'
    readonly_field = ['id',]

class TaskAdmin (admin.ModelAdmin):
    list_display = ()
    #list_filter = ('time_for_work', 'finished_time', 'check_task')


class ContactAdmin (admin.ModelAdmin):
    list_display = ()
    #list_filter = ('id', 'name_c', 'forename_c', 'phone_num', 'birthday_c')
    search_fields = ()


admin.site.register(ToDo, ToDoAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Contact, ContactAdmin)