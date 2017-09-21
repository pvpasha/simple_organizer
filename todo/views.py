from django.shortcuts import render_to_response
from django.shortcuts import render
from todo.models import *
from django.http.response import HttpResponse

def main(request):
    return render(request, 'main.html')

def todo(request):
    return render(request, 'todo.html', {'ToDo': ToDo.objects.all()})

def task(request):
    return render(request, 'task.html', {'Task': Task.objects.all()})

def event(request):
    return render(request, 'event.html', {'Event': Event.objects.all()})

def diary(request):
    return render(request, 'diary.html', {'Diary': Diary.objects.all()})

def budget(request):
    return render(request, 'budget.html', {'Budget': Budget.objects.all()})

def contact(request):
    return render(request, 'contact.html', {'Contact': Contact.objects.all()})

def passorg(request):
    return render(request, 'passorg.html', {'PasswordOrganizer': PasswordOrganizer.objects.all()})

def about(request):
    return render_to_response('about.html')

def test2(request):
    html = "<html><body>THIS TEXT</body></html>"
    return HttpResponse(html)



