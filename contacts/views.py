from django.conf import settings
from django.shortcuts import render, redirect
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from accounts.models import OrganizerUser
from .serializers import ContactListSerializer, ContactSerializer
from .models import Contact
from .forms import ContactForm

class ContactItemView(RetrieveAPIView):
    queryset = Contact.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ContactSerializer
    lookup_field = 'pk'


class ContactListViewSet(ListCreateAPIView):
    queryset = Contact.objects.all()          ## TODO: order_by(owner)
    permission_classes = (AllowAny,)
    serializer_class = ContactListSerializer

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


# def contacts(request):
#     if request.user.is_authenticated():
#         return render(request, 'contacts.html', {'contact_list': Contact.objects.all().filter(owner=request.user),
#                                                'user_avatar': request.user.main_menu_avatar})
#     else:
#         return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))
#
#
# def create_contact(request):
#     if request.user.is_authenticated():
#         if request.method == 'POST':
#             form = ContactForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('/contacts/all/')
#         else: # ==>GET method
#             return render(request, 'create_contact.html', {'form': ContactForm})
#     else:
#         return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))