from django.shortcuts import render,redirect

from .forms import ToDoForm
from .models import ToDO
# Create your views here.


def home(request):
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("tasks")
    form = ToDoForm()
    return render(request,"mytodoapp/index.html",{"form":form})


def tasks(request):
    task=ToDO.objects.all()
    return render(request,"mytodoapp/task.html",{"task":task})


def delete(request,task_id):
    task=ToDO.objects.get(id=task_id)
    task.delete()
    return redirect("tasks")