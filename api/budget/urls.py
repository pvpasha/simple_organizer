from django.conf.urls import url

from . import views as budget_views

# budget/
urlpatterns = [

    url(r'^currency-list/$', budget_views.CurrencyListView.as_view(), name='currency-list'),
    url(r'^currency-create/$', budget_views.CurrencyCreateView.as_view(), name='currency-create'),
    url(r'^currency(?P<pk>.+)/$', budget_views.CurrencyRetrieveUpdateDestroyView.as_view(),
        name='currency-retrieve-update-destroy'),
    url(r'^category-list/$', budget_views.CategoryBudgetListView.as_view(), name='category-list'),
    url(r'^category-create/$', budget_views.CategoryBudgetCreateView.as_view(), name='category-create'),
    url(r'^category(?P<pk>.+)/$', budget_views.CategoryBudgetRetrieveUpdateDestroyView.as_view(),
        name='category-retrieve-update-destroy'),
    url(r'^account-list/$', budget_views.BudgetAccountListView.as_view(), name='budget-account-list'),
    url(r'^account-create/$', budget_views.BudgetAccountCreateView.as_view(), name='account-create'),
    url(r'^account(?P<pk>.+)/$', budget_views.BudgetAccountRetrieveUpdateDestroyView.as_view(),
        name='budget-account-retrieve-update-destroy'),
    url(r'^invoice-list/$', budget_views.InvoiceListView.as_view(), name='invoice-list'),
    url(r'^invoice-create/$', budget_views.InvoiceCreateView.as_view(), name='invoice-create'),
    url(r'^invoice(?P<pk>.+)/$', budget_views.InvoiceRetrieveUpdateDestroyView.as_view(),
        name='invoice-retrieve-update-destroy'),
    url(r'^total-amount-b-a/(?P<budget_account_id>.+)/$', budget_views.TotalAmountByBudgetAccountView.as_view(),
        name='total-amount-by-budget-account'),
    url(r'^total-amount-b-a-list/$', budget_views.TotalAmountByBudgetAccountListView.as_view(),
        name='total-amount-by-budget-account-list'),
    url(r'^total-amount-currency/(?P<currency_id>.+)/$', budget_views.TotalAmountByCurrencyView.as_view(),
        name='total-amount-by-currency'),
    url(r'^total-amount/$', budget_views.TotalAmountView.as_view(),
        name='total-amount'),

]
