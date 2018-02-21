from django.conf.urls import url

from . import views

# budget/
urlpatterns = [
    url(r'^$', views.InvoiceListViewSet.as_view()),

    url(r'^catbud/list/$', views.CategoryBudgetListViewSet.as_view(), name='categorybudget-list'),
    url(r'^catbud/(?P<title>.+)/$', views.CategoryBudgetItemView.as_view(), name='categorybudget-detail'),
    url(r'^currency/list/$', views.CurrencyListViewSet.as_view(), name='currency-list'),
    url(r'^currency/(?P<short_name>.+)/$', views.CurrencyItemView.as_view(), name='currency-detail'),
    url(r'^acctype/list/$', views.AccountTypeListViewSet.as_view(), name='accounttype-list'),
    url(r'^acctype/(?P<short_name>.+)/$', views.AccountTypeItemView.as_view(), name='accounttype-detail'),
    url(r'^budacc/list/$', views.BudgetAccountListViewSet.as_view(), name='budgetaccount-list'),
    url(r'^budacc/(?P<short_name>.+)/$', views.BudgetAccountItemView.as_view(), name='budgetaccount-detail'),
    url(r'^invoice/list/$', views.InvoiceListViewSet.as_view(), name='invoice-list'),
    url(r'^invoice/(?P<pk>.+)/$', views.InvoiceItemView.as_view(), name='invoice-detail'),

    # url(r'^main/$', views.budget),
]