from django.contrib import admin

from .models import *


class CategoryBudgetAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner')
    list_filter = ('title',)
    search_fields = ('id', 'title')
    empty_value_display = '-empty-'
    readonly_field = ['id', ]


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_name', 'owner')
    list_filter = ('name',)
    search_fields = ('id', 'name')
    empty_value_display = '-empty-'
    readonly_field = ['id', ]


class BudgetAccountAdmin (admin.ModelAdmin):
    list_display = ('id', 'owner', 'currency', 'name', 'short_name', 'amount', )
    list_filter = ('currency', 'name', 'short_name')
    search_fields = ('id', 'name')
    empty_value_display = '-empty-'
    readonly_field = ['id', ]


class InvoiceAdmin (admin.ModelAdmin):
    list_display = ('id', 'owner', 'currency', 'amount', 'transaction_type', 'category', 'budget_account',
                    'creation_date')
    list_filter = ('currency', 'amount', 'transaction_type', 'category', 'budget_account')
    search_fields = ('currency', 'amount', 'transaction_type')
    empty_value_display = '-empty-'
    readonly_field = ['id', ]


admin.site.register(CategoryBudget, CategoryBudgetAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(BudgetAccount, BudgetAccountAdmin)
admin.site.register(Invoice, InvoiceAdmin)