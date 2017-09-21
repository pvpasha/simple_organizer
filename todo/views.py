from django.shortcuts import render_to_response
from todo.models import *
from django.http.response import HttpResponse

def main(request):
    return render_to_response('main.html')

def todo(request):
    return render_to_response('todo.html', {'ToDo': ToDo.objects.all()})

def task(request):
    return render_to_response('task.html', {'ToDo': ToDo.objects.all()})

def event(request):
    return render_to_response('event.html', {'ToDo': ToDo.objects.all()})

def budget(request):
    return render_to_response('budget.html', {'ToDo': ToDo.objects.all()})

def contact(request):
    return render_to_response('contact.html', {'ToDo': ToDo.objects.all()})

def passorg(request):
    return render_to_response('passorg.html', {'ToDo': ToDo.objects.all()})

def test2(request):
    html = "<html><body>THIS TEXT</body></html>"
    return HttpResponse(html)



