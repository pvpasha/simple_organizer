from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import OrganizerUser


class CategoryBudget(models.Model):
    title = models.CharField(max_length=30, verbose_name="Payment Category")
    owner = models.ForeignKey(OrganizerUser, on_delete=models.CASCADE)

    def __str__(self):
        return "%d - %s" %(self.pk, self.title)


class Currency(models.Model):
    owner = models.ForeignKey(OrganizerUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    short_name = models.CharField(max_length=3, default="USD")

    def __str__(self):
        return self.short_name


class AccountType(models.Model):
    owner = models.ForeignKey(OrganizerUser, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    short_name = models.CharField(max_length=15)
    credit = models.BooleanField(default=False)
    card = models.BooleanField(default=False)
    perc = models.IntegerField(default=0)
    perc_period = models.IntegerField(default=0, verbose_name="Monthes for percents ADD")

    def __str__(self):
        return "%s - %s" % (self.currency, self.short_name)


class BudgetAccount(models.Model):
    owner = models.ForeignKey(OrganizerUser, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    short_name = models.CharField(max_length=15)
    amount = models.IntegerField(null=True, blank=True, default=0)
    description = models.CharField(max_length=250)
    tax = models.IntegerField(default=0)
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE)

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
    category = models.ForeignKey(CategoryBudget, models.SET_NULL, blank=True, null=True, verbose_name="Payment Category")
    description = models.CharField(max_length=250)
    budget_account = models.ForeignKey(BudgetAccount, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=Invoice, dispatch_uid="update_stock_count")
def update_amount(sender, instance, **kwargs):
    if instance.transaction_type=='income payment':
        instance.budget_account.amount += instance.amount
    elif instance.transaction_type=='outcome payment':
        instance.budget_account.amount -= instance.amount
    instance.budget_account.save()

    #TODO: admin-models, choices invoices, page user login/out, page invoice, page view account
