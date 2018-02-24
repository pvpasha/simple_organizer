from django.conf.urls import url

from . import views as budget_views

# budget/
urlpatterns = [

    url(r'^currency-list/$', budget_views.CurrencyListView.as_view(), name='currency_list'),
    url(r'^currency-create/$', budget_views.CurrencyCreateView.as_view(), name='currency_create'),
    url(r'^currency(?P<pk>.+)/$', budget_views.CurrencyRetrieveUpdateDestroyView.as_view(),
        name='currency_retrieve_update_destroy'),
    url(r'^category-list/$', budget_views.CategoryBudgetListView.as_view(), name='category_list'),
    url(r'^category-create/$', budget_views.CategoryBudgetCreateView.as_view(), name='category_create'),
    url(r'^category(?P<pk>.+)/$', budget_views.CategoryBudgetRetrieveUpdateDestroyView.as_view(),
        name='category_retrieve_update_destroy'),
    url(r'^account-list/$', budget_views.BudgetAccountListView.as_view(), name='budget_account_list'),
    url(r'^account-create/$', budget_views.BudgetAccountCreateView.as_view(), name='account_create'),
    url(r'^account(?P<pk>.+)/$', budget_views.BudgetAccountRetrieveUpdateDestroyView.as_view(),
        name='budget_account_retrieve_update_destroy'),
    url(r'^invoice-list/$', budget_views.InvoiceListView.as_view(), name='invoice_list'),
    url(r'^invoice-create/$', budget_views.InvoiceCreateView.as_view(), name='invoice_create'),
    url(r'^invoice(?P<pk>.+)/$', budget_views.InvoiceRetrieveUpdateDestroyView.as_view(),
        name='invoice_retrieve_update_destroy'),

]
