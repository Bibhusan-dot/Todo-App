from django.shortcuts import *
from .models import todo
from django.template import loader
from django.http import HttpResponse

def todo_list(request):
    todos = todo.objects.all()

    if request.method == "POST":
        if "add_task" in request.POST:
            name = request.POST.get("name")
            if name:
                todo.objects.create(name=name)
            return redirect("todo_list")
        if "edit_task" in request.POST:
            taskId = request.POST.get("task_id")
            newname = request.POST.get("new_name")
            Todo = get_object_or_404(todo,id=taskId)
            Todo.name = newname
            Todo.save()
            return redirect("todo_list")
        if "delete_task" in request.POST:
            taskId = request.POST.get("task_id")
            Todo = get_object_or_404(todo,id=taskId)
            Todo.delete()
            return redirect("todo_list")
        if "clear_all" in request.POST:
            todo.objects.all().delete()
            return redirect("todo_list")
    context = {
        "todos":todos
    }
    return render(request,"todo.html",context)