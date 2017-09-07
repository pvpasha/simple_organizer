from django.contrib import admin

from .models import OrganizerUser


class OrganizerUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'second_name', 'user_mail')
    list_filter = ( 'first_name', 'second_name', 'user_mail')
    search_fields = ('first_name', 'second_name', 'user_mail')
    empty_value_display = '-empty-'
    readonly_field = ['id',]


admin.site.register(OrganizerUser, OrganizerUserAdmin)