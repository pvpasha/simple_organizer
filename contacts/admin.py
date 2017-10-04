from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'surname', 'phone', 'add_reminder')
    list_filter = ('owner',)
    search_fields = ('id', 'name', 'surname', 'phone')
    empty_value_display = '-empty-'
    readonly_field = ['id', ]

admin.site.register(Contact, ContactAdmin)