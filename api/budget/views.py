import logging

from rest_framework import status, exceptions
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import (ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from django_filters.rest_framework import DjangoFilterBackend

from accounts.models import OrganizerUser as User
from .models import Currency, CategoryBudget, BudgetAccount, Invoice
from .serializers import CurrencySerializer, CategoryBudgetSerializer, BudgetAccountSerializer, InvoiceSerializer
from .filters import InvoiceFilter, BudgetAccountFilter


logger = logging.getLogger(__name__)


class CurrencyListView(ListAPIView):
    serializer_class = CurrencySerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'owner'

    def get_queryset(self):
        try:
            return Currency.objects.filter(owner=self.request.user.id)
        except ObjectDoesNotExist:
            logger.error('Object not found for user with ID #%s for currency_list_view' % self.request.user.id)
            raise exceptions.NotFound('Object with your ID %s NotFound' % self.request.user.id)


class CurrencyCreateView(CreateAPIView):
    serializer_class = CurrencySerializer
    permission_classes = (IsAuthenticated,)
    queryset = Currency.objects.all()

    def post(self, request, *args, **kwargs):
        if request.data['name'] and request.data['short_name']:
            try:
                user = User.objects.get(pk=self.request.user.id)
                currency = Currency.objects.create(owner=user,
                                                   name=request.data['name'],
                                                   short_name=request.data['short_name'])
                serializer = self.get_serializer(currency)
                logger.info('Currency created with short_name #%s for user ID #%s in currency_create_view'
                            % (request.data['short_name'], self.request.user.id))
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ObjectDoesNotExist:
                logger.error('Error creation currency by user ID #%s in currency_create_view' % self.request.user.id)
                raise exceptions.FieldError('Error creation currency. Pleas check your data in request')
        else:
            logger.error('Data in request are wrong with user ID #%s in currency_create_view'
                         % self.request.user.id)
            raise exceptions.ValidationError('Data in request are wrong')


class CurrencyRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CurrencySerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'pk'

    def get_queryset(self):
        try:
            instance = Currency.objects.filter(owner=self.request.user.id)
            return instance
        except ObjectDoesNotExist:
            logger.error('Not found object with ID #%s and user ID #%s for currency_retrieve_update'
                         % self.kwargs['pk'], self.request.user.id)
            raise exceptions.NotFound('Object not found')


class CategoryBudgetListView(ListAPIView):
    serializer_class = CategoryBudgetSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'owner'

    def get_queryset(self):
        try:
            return CategoryBudget.objects.filter(owner=self.request.user.id)
        except ObjectDoesNotExist:
            logger.error('Object not found for user with ID #%s for category_budget_list_view' % self.request.user.id)
            raise exceptions.NotFound('Object with your ID %s NotFound' % self.request.user.id)


class CategoryBudgetCreateView(CreateAPIView):
    serializer_class = CategoryBudgetSerializer
    permission_classes = (IsAuthenticated,)
    queryset = CategoryBudget.objects.all()

    def post(self, request, *args, **kwargs):
        if request.data['title']:
            try:
                user = User.objects.get(pk=self.request.user.id)
                new_obj = CategoryBudget.objects.create(owner=user, title=request.data['title'])
                serializer = self.get_serializer(new_obj)
                logger.info('Category created with title #%s for user ID #%s in category_budget_create_view'
                            % (request.data['title'], self.request.user.id))
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ObjectDoesNotExist:
                logger.error('Error creation category by user ID #%s in category_budget_view' % self.request.user.id)
                raise exceptions.FieldError('Error creation currency. Pleas check your data in request')
        else:
            logger.error('Data in request are wrong with user ID #%s in category_budget_create_view'
                         % self.request.user.id)
            raise exceptions.ValidationError('Data in request are wrong')


class CategoryBudgetRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryBudgetSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'pk'

    def get_queryset(self):
        try:
            return CategoryBudget.objects.filter(owner=self.request.user.id)
        except ObjectDoesNotExist:
            logger.error('CategoryBudget for user %s and ID #%s not found for category_budget_retrieve_update_view'
                         % self.request.user.email, self.kwargs['pk'])
            raise exceptions.NotFound('Category with ID not found')


class BudgetAccountListView(ListAPIView):
    serializer_class = BudgetAccountSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filter_class = BudgetAccountFilter

    def get_queryset(self):
        try:
            return BudgetAccount.objects.filter(owner=self.request.user.id)
        except ObjectDoesNotExist:
            logger.error('Object not found for user with ID #%s for budget_account_list_view' % self.request.user.id)
            raise exceptions.NotFound('Object with your ID %s NotFound' % self.request.user.id)


class BudgetAccountCreateView(CreateAPIView):
    serializer_class = BudgetAccountSerializer
    permission_classes = (IsAuthenticated,)
    queryset = BudgetAccount.objects.all()

    def post(self, request, *args, **kwargs):
        if request.data:
            try:
                user = User.objects.get(pk=self.request.user.id)
                currency = Currency.objects.get(pk=request.data['currency'])
                new_obj = BudgetAccount.objects.create(owner=user,
                                                       name=request.data['name'],
                                                       short_name=request.data['short_name'],
                                                       amount=request.data['amount'],
                                                       description=request.data['description'],
                                                       currency=currency)
                serializer = self.get_serializer(new_obj)
                logger.info('Budget account created with name #%s for user ID #%s in budget_account_create_view'
                            % (request.data['name'], self.request.user.id))
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ObjectDoesNotExist:
                logger.error('Error creation category by user ID #%s in budget_account_create_view'
                             % self.request.user.id)
                raise exceptions.FieldError('Error creation currency. Pleas check your data in request')
        else:
            logger.error('Data in request are wrong with user ID #%s in budget_account_create_view'
                         % self.request.user.id)
            raise exceptions.ValidationError('Data in request are wrong')


class BudgetAccountRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = BudgetAccountSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'pk'

    def get_queryset(self):
        try:
            return BudgetAccount.objects.filter(owner=self.request.user.id)
        except ObjectDoesNotExist:
            logger.error('BudgetAccount for user %s and ID #%s not found for budget_account_retrieve_update_view'
                         % self.request.user.email, self.kwargs['pk'])
            raise exceptions.NotFound('Account with ID not found')


class InvoiceListView(ListAPIView):
    serializer_class = InvoiceSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filter_class = InvoiceFilter

    def get_queryset(self):
        try:
            return Invoice.objects.filter(owner=self.request.user.id)
        except ObjectDoesNotExist:
            logger.error('Object not found for user with ID #%s for invoice_list_view' % self.request.user.id)
            raise exceptions.NotFound('Object with your ID %s NotFound' % self.request.user.id)


class InvoiceCreateView(CreateAPIView):
    serializer_class = InvoiceSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Invoice.objects.all()

    def post(self, request, *args, **kwargs):
        if request.data:
            try:
                user = User.objects.get(pk=self.request.user.id)
                currency = Currency.objects.get(pk=request.data['currency'])
                category = CategoryBudget.objects.get(pk=request.data['category'])
                budget_account = BudgetAccount.objects.get(pk=request.data['budget_account'])
                new_obj = Invoice.objects.create(owner=user,
                                                 amount=request.data['amount'],
                                                 transaction_type=request.data['transaction_type'],
                                                 description=request.data['description'],
                                                 currency=currency,
                                                 category=category,
                                                 budget_account=budget_account)
                serializer = self.get_serializer(new_obj)
                logger.info('Invoice created for user ID #%s in invoice_create_view' % self.request.user.id)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ObjectDoesNotExist:
                logger.error('Error creation invoice by user ID #%s in invoice_create_view' % self.request.user.id)
                raise exceptions.FieldError('Error creation currency. Pleas check your data in request')
        else:
            logger.error('Data in request are wrong with user ID #%s in invoice_create_view'
                         % self.request.user.id)
            raise exceptions.ValidationError('Data in request are wrong')


class InvoiceRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = InvoiceSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'pk'

    def get_queryset(self):
        try:
            instance = Invoice.objects.filter(owner=self.request.user.id)
            return instance
        except ObjectDoesNotExist:
            logger.error('Invoice ID #%s and user %s not found for invoice_retrieve_update_view'
                         % self.kwargs['pk'], self.request.user.email)
            raise exceptions.NotFound('Invoice with ID #%s not found' % self.kwargs['pk'])


class TotalAmountByBudgetAccountView(APIView):
    # authentication_classes = (BaseAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, budget_account_id):
        try:
            res = {
                "total": 0,
                "total_invoices": 0
            }
            user = User.objects.get(pk=request.user.id)
            budget_account = BudgetAccount.objects.filter(pk=budget_account_id)
            invoice_list = Invoice.objects.filter(budget_account=budget_account)
            for invoice in invoice_list:
                if user.id == invoice.owner.id:
                    res['total_invoices'] += 1
                    res['total'] += invoice.amount if invoice.transaction_type else -invoice.amount
        except ObjectDoesNotExist:
            logger.error('Can not get total amount for %s with budget ID #%s in total_amount_by_budget_account_view'
                         % (request.user.id, budget_account_id))
            return Response({"detail": "Can not get total amount for %s with budget ID #%s" % (
                request.user.id, budget_account_id)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(res, status=status.HTTP_200_OK)


class TotalAmountByBudgetAccountListView(APIView):  # TODO: Make list of budget_accounts in response
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            res = {
                "budget_account_id": 0,
                "total": 0,
                "total_invoices": 0
            }
            user = User.objects.get(pk=request.user.id)
            budget_account_list = BudgetAccount.objects.filter(owner=request.user.id)
            for budget_account in budget_account_list:
                invoice_list = Invoice.objects.filter(budget_account=budget_account.id)
                for invoice in invoice_list:
                    if user.id == invoice.owner.id:
                        res['budget_account_id'] = budget_account.id
                        res['total_invoices'] += 1
                        res['total'] += invoice.amount if invoice.transaction_type else -invoice.amount
        except ObjectDoesNotExist:
            logger.error('Can"t get total amount for %s with budget ID #%s in total_amount_by_budget_account_list_view'
                         % (request.user.id, budget_account.id))
            return Response({"detail": "Can not get total amount for %s with budget ID #%s" % (
                request.user.id, budget_account.id)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(res, status=status.HTTP_200_OK)


class TotalAmountByCurrencyView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, currency_id):
        try:
            res = {
                "total": 0,
                "total_invoices": 0
            }
            user = User.objects.get(pk=request.user.id)
            currency = Currency.objects.filter(pk=currency_id)
            invoice_list = Invoice.objects.filter(currency=currency)
            for invoice in invoice_list:
                if user.id == invoice.owner.id:
                    res['total_invoices'] += 1
                    res['total'] += invoice.amount if invoice.transaction_type else -invoice.amount
        except ObjectDoesNotExist:
            logger.error('Can not get total amount for %s with currency ID #%s in total_amount_by_currency_view'
                         % (request.user.id, currency_id))
            return Response({"detail": "Can not get total amount for %s with currency ID #%s" % (
                request.user.id, currency_id)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(res, status=status.HTTP_200_OK)


class TotalAmountView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            res = {
                "total": 0,
                "total_invoices": 0
            }
            user = User.objects.get(pk=request.user.id)
            invoice_list = Invoice.objects.all()
            for invoice in invoice_list:
                if user.id == invoice.owner.id:
                    res['total_invoices'] += 1
                    res['total'] += invoice.amount if invoice.transaction_type else -invoice.amount
        except ObjectDoesNotExist:
            logger.error('Can not get total amount for %s in total_amount_view' % request.user.id)
            return Response({"detail": "Can not get total amount for %s" % request.user.id},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(res, status=status.HTTP_200_OK)
