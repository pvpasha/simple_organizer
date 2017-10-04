from django.contrib import admin

from .models import *


class DiaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'creation_date')
    list_filter = ('title', 'creation_date')
    search_fields = ('id', 'title')
    empty_value_display = '-empty-'
    readonly_field = ['id',]

admin.site.register(Diary, DiaryAdmin)