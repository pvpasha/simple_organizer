from django.conf.urls import url

from . import views as budget_views

# budget/
urlpatterns = [

    url(r'^account-type-list/$', budget_views.AccountTypeListView.as_view(), name='account_type_list'),
    url(r'^account-type(?P<pk>.+)/$', budget_views.AccountTypeRetUpdView.as_view(), name='account_type_ret_upd'),

    url(r'^account-list/$', budget_views.BudgetAccountListView.as_view(), name='budget_account_list'),
    url(r'^account(?P<pk>.+)/$', budget_views.BudgetAccountRetUpdView.as_view(), name='budget_account_ret_upd'),

    url(r'^currency-list/$', budget_views.CurrencyListView.as_view(), name='currency_list'),
    url(r'^currency(?P<pk>.+)/$', budget_views.CurrencyRetUpdView.as_view(), name='currency_ret_upd'),

    url(r'^category-list/$', budget_views.CategoryBudgetListView.as_view(), name='category_list'),
    url(r'^category(?P<pk>.+)/$', budget_views.CategoryBudgetRetUpdView.as_view(),  name='category_ret_upd'),

    url(r'^invoice-list/$', budget_views.InvoiceListView.as_view(), name='invoice_list'),
    url(r'^invoice(?P<pk>.+)/$', budget_views.InvoiceRetUpdView.as_view(), name='invoice_red_upd'),


]