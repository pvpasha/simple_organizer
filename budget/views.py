from rest_framework.permissions import AllowAny
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from accounts.models import OrganizerUser
from .models import CategoryBudget, Currency, AccountType, BudgetAccount, Invoice
from .serializers import (CategoryBudgetListSerializer, CategoryBudgetSerializer, CurrencySerializer,
                          CurrencyListSerializer, AccountTypeListSerializer, AccountTypeSerializer,
                          BudgetAccountListSerializer, BudgetAccountSerializer, InvoiceSerializer,
                          InvoiceListSerializer)


class CategoryBudgetItemView(RetrieveAPIView):
    queryset = CategoryBudget.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CategoryBudgetSerializer
    lookup_field = 'title'


class CategoryBudgetListViewSet(ListCreateAPIView):
    queryset = CategoryBudget.objects.all()          ## TODO: order_by(owner)
    permission_classes = (AllowAny,)
    serializer_class = CategoryBudgetListSerializer
    # lookup_field = 'title'

    # def post(self, request):
    #     get_owner = request.data['owner']
    #     get_title = request.data['title']
    #     get_body = request.data['body']
    #
    #     try:
    #         user = OrganizerUser.objects.get(pk=get_owner)
    #         diary_item = Diary.objects.create(owner=user, title=get_title, body=get_body)
    #         serialized_data =self.get_serializer(diary_item)
    #         return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    #     except ObjectDoesNotExist:
    #         return Response({'detail': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)


class CurrencyItemView(RetrieveAPIView):
    queryset = Currency.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CurrencySerializer
    lookup_field = 'short_name'


class CurrencyListViewSet(ListCreateAPIView):
    queryset = Currency.objects.all()          ## TODO: order_by(owner)
    permission_classes = (AllowAny,)
    serializer_class = CurrencyListSerializer


class AccountTypeItemView(RetrieveAPIView):
    queryset = AccountType.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = AccountTypeSerializer
    lookup_field = 'short_name'


class AccountTypeListViewSet(ListCreateAPIView):
    queryset = AccountType.objects.all()          ## TODO: order_by(owner)
    permission_classes = (AllowAny,)
    serializer_class = AccountTypeListSerializer


class BudgetAccountItemView(RetrieveAPIView):
    queryset = BudgetAccount.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = BudgetAccountSerializer
    lookup_field = 'short_name'


class BudgetAccountListViewSet(ListCreateAPIView):
    queryset = BudgetAccount.objects.all()          ## TODO: order_by(owner)
    permission_classes = (AllowAny,)
    serializer_class = BudgetAccountListSerializer


class InvoiceItemView(RetrieveAPIView):
    queryset = Invoice.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = InvoiceSerializer


class InvoiceListViewSet(ListCreateAPIView):
    queryset = Invoice.objects.all()          ## TODO: order_by(owner)
    permission_classes = (AllowAny,)
    serializer_class = InvoiceListSerializer


# def budget(request):
#     #html = '<h1 style="color: red;">You have %d invoice(s)</h1>' % len(Invoice.objects.all().filter(owner=request.user))
#     if request.user.is_authenticated():
#     #    return HttpResponse(html, status=200)
#         return render(request, 'budget.html', {'invoice_list': Invoice.objects.all().filter(owner=request.user),
#                                                'user_avatar': request.user.main_menu_avatar})
#     else:
#         return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))