from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import TodoApp
# Create your views here.


def add_item(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = TodoForm()
        else:
            todo = TodoApp.objects.get(pk=id)
            form = TodoForm(instance=todo)

        return render(request, 'add_item.html', {'form': form})
    else:
        if id == 0:
            form = TodoForm(request.POST)
        else:
            todo = TodoApp.objects.get(pk=id)
            form = TodoForm(request.POST, instance=todo)
    if form.is_valid():
        form.save()
    return redirect('/todo/list')


def item_list(request):
    context = {'item_list': TodoApp.objects.all()}
    return render(request, "item_list.html", context)


def delete_item(request, id):
    todo = TodoApp.objects.get(pk=id)
    todo.delete()
    return redirect('/todo/list')
