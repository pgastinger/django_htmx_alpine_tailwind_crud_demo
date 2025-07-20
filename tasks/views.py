# tasks/views.py

from django.http import HttpResponse
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
    Triggered by HTMX on page load or when a task is added/updated.
    """
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_create(request):
    """
    Handles creating a new task.
    On POST, it saves the task and returns an empty response with two key headers:
    - HX-Reswap: 'none' tells HTMX not to swap any content.
    - HX-Trigger: tells HTMX to fire events to refresh the list and close the modal.
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            response = HttpResponse() # Return an empty 200 OK response
            response['HX-Trigger'] = '{"taskAdded": null, "close-modal": null}'
            return response
    else:
        form = TaskForm()
    return render(request, 'tasks/partials/task_form.html', {'form': form})

def task_update(request, pk):
    """
    Handles updating an existing task.
    On POST, it saves the changes and triggers the same events as task creation.
    """
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            response = HttpResponse() # Return an empty 200 OK response
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
    return HttpResponse(status=405) # Method Not Allowed

def task_delete(request, pk):
    """
    Deletes a task. Returns an empty response, which tells HTMX to
    remove the element from the DOM.
    """
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return HttpResponse(status=200)   
    return HttpResponse(status=405) # Method Not Allowed
