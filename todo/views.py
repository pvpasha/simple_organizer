from django.shortcuts import render_to_response
from todo.models import *
from django.http.response import HttpResponse

def main(request):
    return render_to_response('main.html')

def todo(request):
    return render_to_response('todo.html', {'ToDo': ToDo.objects.all()})

def task(request):
    return render_to_response('task.html', {'Task': Task.objects.all()})

def event(request):
    return render_to_response('event.html', {'Event': Event.objects.all()})

def diary(request):
    return render_to_response('diary.html', {'Diary': Diary.objects.all()})

def budget(request):
    return render_to_response('budget.html', {'Budget': Budget.objects.all()})

def contact(request):
    return render_to_response('contact.html', {'Contact': Contact.objects.all()})

def passorg(request):
    return render_to_response('passorg.html', {'PasswordOrganizer': PasswordOrganizer.objects.all()})

def about(request):
    return render_to_response('about.html')

def test2(request):
    html = "<html><body>THIS TEXT</body></html>"
    return HttpResponse(html)



