from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from .models import todolist  # Use the correct model name
from .forms import TodoListForm  # Make sure the form matches the model
from django.contrib import messages
from datetime import date, timedelta

# View for home page

def home(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            task_id = request.POST.get('task_id')
            if task_id:
                # Update existing task
                task = todolist.objects.get(pk=task_id)
                form = TodoListForm(request.POST, instance=task)
            form.save()
            messages.success(request, "Task saved successfully!")
            return redirect('home')  # Stay on the same page
        else:
            messages.error(request, "There was an error with the form.")
    else:
        form = TodoListForm()

    tasks = todolist.objects.all()
    showing_completed = request.GET.get('completed') == 'true'
    if showing_completed:
        tasks = tasks.filter(status='Completed')

    for task in tasks:
        if task.due_date:
            task.is_due_soon = (task.due_date - date.today()).days <= 3
        else:
            task.is_due_soon = False

    delete_id = request.GET.get('delete_id')
    if delete_id:
        todolist.objects.filter(id=delete_id).delete()
        messages.success(request, "Task deleted successfully.")
        return redirect('home')

    return render(request, 'base.html', {
        'form': form,
        'tasks': tasks,
        'showing_completed': showing_completed
    })


def login(request):
    return render(request, 'login.html')

