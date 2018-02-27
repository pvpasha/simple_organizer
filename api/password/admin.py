from django.contrib import admin

from .models import PasswordOrganizer


class PasswordOrganizerAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'resource_url')
    list_filter = ('owner',)
    search_fields = ('id', 'resource_url')
    empty_value_display = '-empty-'
    readonly_field = ['id', ]


admin.site.register(PasswordOrganizer, PasswordOrganizerAdmin)
