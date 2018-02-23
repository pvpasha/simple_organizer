from django_filters import rest_framework as filters

from .models import Invoice, BudgetAccount


class InvoiceFilter(filters.FilterSet):
    min_amount = filters.NumberFilter(name='amount', lookup_expr='gte')
    max_amount = filters.NumberFilter(name='amount', lookup_expr='lte')
    creation_date = filters.IsoDateTimeFilter()

    class Meta:
        model = Invoice
        fields = ['currency', 'category', 'budget_account', 'transaction_type', 'min_amount', 'max_amount',
                  'creation_date']


class BudgetAccountFilter(filters.FilterSet):
    min_amount = filters.NumberFilter(name='amount', lookup_expr='gte')
    max_amount = filters.NumberFilter(name='amount', lookup_expr='lte')

    class Meta:
        model = BudgetAccount
        fields = ['currency', 'min_amount', 'max_amount']

        # fields = {
        #     'username': ['exact', 'contains'],
        #     'last_login': ['exact', 'year__gt'],
        # }
