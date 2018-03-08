from django.db import models

from accounts.models import OrganizerUser


class Currency(models.Model):
    owner = models.ForeignKey(OrganizerUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=5)

    def __str__(self):
        return self.short_name


class CategoryBudget(models.Model):
    owner = models.ForeignKey(OrganizerUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class BudgetAccount(models.Model):
    owner = models.ForeignKey(OrganizerUser, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=20)
    amount = models.IntegerField(null=True, blank=True, default=0)
    description = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return "%s - %s" % (self.currency, self.short_name)


class Invoice(models.Model):
    owner = models.ForeignKey(OrganizerUser, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True, blank=True, default=0)

    INCOME = True
    OUTCOME = False

    TT_CHOICES = (
        (INCOME, 'Income'),
        (OUTCOME, 'Outcome')
    )
    transaction_type = models.IntegerField(choices=TT_CHOICES, default=INCOME)
    category = models.ForeignKey(CategoryBudget, models.SET_NULL, blank=True, null=True)
    description = models.CharField(max_length=250)
    budget_account = models.ForeignKey(BudgetAccount, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    # TODO: make 'transaction_type' return 'INCOME' text

