from django.shortcuts import render
from django.views.generic import TemplateView


def home(request):
    if request.user.is_authenticated():
        return render(request, 'home.html', {'user_avatar_big': request.user.main_menu_avatar_big,
                                             'user_avatar': request.user.main_menu_avatar})
    else:
        return render(request, 'home.html', {'user_avatar_big': "-empty-"})


def about(request):
    if request.user.is_authenticated():
        return render(request, 'about.html', {'user_avatar_big': request.user.main_menu_avatar_big,
                                             'user_avatar': request.user.main_menu_avatar})
    else:
        return render(request, 'about.html', {'user_avatar_big': "-empty-"})


# class HomeView(TemplateView):
#     template_name = 'home.html'
#
#     def home(self, request):
#         if request.user.is_authenticated():
#             return render(request, 'home.html', {'user_avatar_big': request.user.main_menu_avatar_big,
#                                                 'user_avatar': request.user.main_menu_avatar})
#         else:
#             return render(request, 'home.html', {'user_avatar_big': "-empty-"})
