from django.shortcuts import render,redirect
from .forms import TaskForm
from .models import Task
from django.contrib import messages
# Create your views here.
def index_view(request):
    tasks = Task.objects.all()
    return render(request,"index.html",{
        'tasks':tasks,
    })

def add_task(request):
    if request.method == 'POST':
        task = request.POST['task']
        task_obj = Task.objects.create(task_name=task)
        task_obj.save()
        return redirect('index')
    else:
        return redirect('index')


def edit_task(request,id):
    if request.method == 'POST':
        task = Task.objects.get(pk=id)
        task.task_name = request.POST['task']
        task.save()
        return redirect('index')
       
    else:
        task = Task.objects.get(pk=id)
        return render(request,"index.html",{
            'task':task,
        })

def update_task(request,id):
    if request.method == 'POST':
        task = Task.objects.get(pk=id)
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            updated_task = form.save()
            return redirect('index')
        else:
            messages.error(request, 'Failed to update task.')
    else:
        task = Task.objects.get(pk=id)
        form = TaskForm(instance=task)
        return render(request,"index.html",{
            'form':form,
            'task':task,
        })


def delete_task(request,id):
    task = Task.objects.get(pk=id)  
    task.delete() 
    return redirect('index')

#Is the task completed
def done_task_view(request,id):
    task = Task.objects.get(pk=id)  
    if task.completed == False:
        task.completed =True
        task.save()
        return redirect('index')


def undo_task_view(request,id):
    task = Task.objects.get(pk=id)  
    if task.completed == True:
        task.completed =False
        task.save()
        return redirect('index')

