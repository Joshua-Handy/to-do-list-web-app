from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import todolist
from .forms import TodoListForm
from datetime import date


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            if user.is_staff:
                return redirect('task_panel_admin')
            else:
                return redirect('task_panel_user')
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'login.html')


@login_required
def task_panel_admin(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            task_id = request.POST.get('task_id')
            if task_id:
                task = todolist.objects.get(pk=task_id)
                form = TodoListForm(request.POST, instance=task)
            form.save()
            messages.success(request, "Task saved successfully!")
            return redirect('task_panel_admin')
        else:
            messages.error(request, "There was an error with the form.")
    else:
        form = TodoListForm()

    tasks = todolist.objects.all()
    showing_completed = request.GET.get('completed') == 'true'
    showing_pending = request.GET.get('pending') == 'true'

    if showing_completed:
        tasks = tasks.filter(status__iexact='Completed')
    elif showing_pending:
        tasks = tasks.exclude(status__iexact='Completed')

    for task in tasks:
        if task.due_date:
            task.is_due_soon = (task.due_date - date.today()).days <= 3
        else:
            task.is_due_soon = False
        task.is_completed = task.status.lower() == 'completed'

    delete_id = request.GET.get('delete_id')
    if delete_id:
        todolist.objects.filter(id=delete_id).delete()
        messages.success(request, "Task deleted successfully.")
        return redirect('task_panel_admin')

    return render(request, 'taskPanel.html', {
        'form': form,
        'tasks': tasks,
        'showing_completed': showing_completed,
        'showing_pending': showing_pending,
    })


@login_required
def task_panel_user(request):
    tasks = todolist.objects.all()

    showing_completed = request.GET.get('completed') == 'true'
    showing_pending = request.GET.get('pending') == 'true'

    if showing_completed:
        tasks = tasks.filter(status__iexact='Completed')
    elif showing_pending:
        tasks = tasks.exclude(status__iexact='Completed')

    for task in tasks:
        if task.due_date:
            task.is_due_soon = (task.due_date - date.today()).days <= 3
        else:
            task.is_due_soon = False
        task.is_completed = task.status.lower() == 'completed'

    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        new_status = request.POST.get('status')
        if task_id and new_status:
            try:
                task = todolist.objects.get(pk=task_id)
                task.status = new_status
                task.save()
                messages.success(request, f"Task {task.name} updated.")
            except todolist.DoesNotExist:
                messages.error(request, "Task not found.")
        return redirect('task_panel_user')

    return render(request, 'taskPanel_user.html', {
        'tasks': tasks,
        'showing_completed': showing_completed,
        'showing_pending': showing_pending,
    })
