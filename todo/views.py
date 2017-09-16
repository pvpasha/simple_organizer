from django.shortcuts import render_to_response
from todo.models import *

from django.http.response import HttpResponse

# Create your views here.
def todo(request):
    return render_to_response('main.html', {'git ': ToDo.objects.all()})


def test2(request):
	html = "<html><body>THIS TEXT</body></html>"
	return HttpResponse(html)



