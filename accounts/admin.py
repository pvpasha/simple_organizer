from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

from .forms import UserChangeForm, UserCreationForm
from .models import OrganizerUser


class OrganizerUserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('id', 'first_name', 'second_name', 'user_mail')
    list_filter = ('first_name', 'second_name', 'user_mail')

    fieldsets = (
        (None, {'fields': ('user_mail', 'password')}),
        ('Personal info', {'fields': ('first_name', 'second_name', 'is_staff',
                                      'is_active', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {'fields': ('user_mail', 'password1', 'password2')}),
        ('Extra info', {'classes': ('collapse',),
                        'fields': ('first_name', 'second_name')}),
    )

    search_fields = ('first_name', 'second_name', 'user_mail')
    empty_value_display = '-empty-'
    readonly_field = ['id',]

    ordering = ('user_mail',)


admin.site.register(OrganizerUser, OrganizerUserAdmin)