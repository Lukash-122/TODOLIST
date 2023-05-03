from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import TodoappItem


def TodoappView(request):
    todolist = TodoappItem.objects.all()
    return render(request, 'todoapp/index.html', {'todolist': todolist})


def addTodoView(request):
    content = request.POST['content']
    new_item = TodoappItem(content=content)
    new_item.save()
    return HttpResponseRedirect('/todo/')


def DeleteItem(request, item):
    obj = TodoappItem.objects.get(pk=item)
    obj.delete()
    return HttpResponseRedirect('/todo/')
