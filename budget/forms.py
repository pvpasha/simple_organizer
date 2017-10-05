from django import forms

from .models import BudgetAccount


class BudgetForm(forms.ModelForm):

    class Meta:
        model = BudgetAccount
        fields = ('owner', 'title', 'body')