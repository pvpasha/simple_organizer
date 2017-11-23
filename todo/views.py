from django.shortcuts import render


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