from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

from .forms import UserChangeForm, UserCreationForm
from .models import OrganizerUser


class OrganizerUserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('id', 'username', 'second_name', 'email', 'image_thumb', 'avatar',  'create_at',
                    'update_at')
    list_filter = ('username', 'second_name', 'email')

    fieldsets = (
        (None, {'fields': ('email', 'password', 'avatar')}),
        ('Personal info', {'fields': ('username', 'second_name', 'is_staff',
                                      'is_active')}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2')}),
        ('Extra info', {'classes': ('collapse',),
                        'fields': ('username', 'second_name', 'avatar')}),
    )

    search_fields = ('username', 'second_name', 'email')
    empty_value_display = '-empty-'
    readonly_field = ['image_thumb']
    ordering = ('email',)


admin.site.register(OrganizerUser, OrganizerUserAdmin)
