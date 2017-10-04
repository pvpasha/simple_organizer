from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http.response import HttpResponse


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

def about(request):
    return render_to_response('about.html')

def test2(request):
    html = "<html><body>THIS TEXT</body></html>"
    return HttpResponse(html)