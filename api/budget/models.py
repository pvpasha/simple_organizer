from django.db import models

from accounts.models import OrganizerUser


class CategoryBudget(models.Model):
    owner = models.ForeignKey(OrganizerUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)

    def __str__(self):
        return "%d - %s" % (self.pk, self.title)


class Currency(models.Model):
    owner = models.ForeignKey(OrganizerUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default='United States Dollar')
    short_name = models.CharField(max_length=5, default='USD')

    def __str__(self):
        return self.short_name


class BudgetAccount(models.Model):
    owner = models.ForeignKey(OrganizerUser, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    short_name = models.CharField(max_length=10)
    amount = models.IntegerField(null=True, blank=True, default=0)
    description = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return "%s - %s" % (self.currency, self.short_name)


class Invoice(models.Model):
    owner = models.ForeignKey(OrganizerUser, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True, blank=True, default=0)

    INCOME = 1
    OUTCOME = -1

    TT_CHOICES = (
        (INCOME, 'Income'),
        (OUTCOME, 'Outcome')
    )
    transaction_type = models.IntegerField(choices=TT_CHOICES, default=INCOME)
    category = models.ForeignKey(CategoryBudget, models.SET_NULL, blank=True, null=True)
    description = models.CharField(max_length=250)
    budget_account = models.ForeignKey(BudgetAccount, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
