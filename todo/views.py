from django.shortcuts import render, render_to_response


def main(request):
    if request.user.is_authenticated():
        return render(request, 'main.html', {'user_avatar_big': request.user.main_menu_avatar_big,
                                             'user_avatar': request.user.main_menu_avatar})
    else:
        return render(request, 'main.html', {'user_avatar_big': "-empty-"})

# def template(request):
#     if request.user.is_authenticated():
#         return render(request, 'template.html', {'user_avatar': request.user.main_menu_avatar})
#     else:
#         return render(request, 'template.html', {'user_avatar': "-empty-"})


def about():
    return render_to_response('about.html')
