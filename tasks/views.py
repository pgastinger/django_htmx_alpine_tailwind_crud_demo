# tasks/views.py

from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import Task
from .forms import TaskForm

def index(request):
    """
    Renders the main page. The task list itself is loaded asynchronously by HTMX.
    """
    return render(request, 'tasks/index.html')

def task_list(request):
    """
    Returns an HTML fragment containing the list of tasks.
    """
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_create(request):
    """
    Handles creating a new task. On success, it triggers events to close the
    modal and refresh the task list. This event-based approach is best for modals.
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            response = HttpResponse()
            response['HX-Reswap'] = 'none'
            response['HX-Trigger'] = '{"taskAdded": null, "close-modal": null}'
            return response
    else:
        form = TaskForm()
    return render(request, 'tasks/partials/task_form.html', {'form': form})

def task_update(request, pk):
    """
    Handles updating an existing task. On success, it triggers events to close the
    modal and refresh the task list.
    """
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            response = HttpResponse()
            response['HX-Reswap'] = 'none'
            response['HX-Trigger'] = '{"taskAdded": null, "close-modal": null}'
            return response
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/partials/task_form.html', {'form': form, 'task': task})

def task_toggle(request, pk):
    """
    Toggles the 'completed' status of a task.
    Returns the updated task detail partial to be swapped in the list.
    """
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=pk)
        task.completed = not task.completed
        task.save()
        return render(request, 'tasks/partials/task_detail.html', {'task': task})
    return HttpResponse(status=405)

def task_delete(request, pk):
    """
    Deletes a task. If it's the last task, it triggers a page redirect via
    the HX-Redirect header. Otherwise, it returns the updated task list.
    """
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=pk)
        task.delete()

        # Check if any tasks are left
        if not Task.objects.exists():
            response = HttpResponse()
            # This header tells HTMX to do a full page redirect to the index page.
            response['HX-Redirect'] = reverse('index')
            return response
        return HttpResponse(status=200)   

    return HttpResponse(status=405)
