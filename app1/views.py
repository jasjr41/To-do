from django.shortcuts import render, get_object_or_404, redirect
from app1.forms import TaskForm
from app1.models import Task


def index(request):
    to_do = Task.objects.all()

    if request.method == 'POST':

        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to avoid duplicate form submissions
            return redirect('index')
    else:
        form = TaskForm()

    context = {'to_do': to_do, 'form': form}
    return render(request, "index.html", context)
def delete(request, id):
    task = get_object_or_404(Task, pk=id)
    if request.method == 'POST':
        task.delete()
        return redirect('index')

def update(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(request.POST, instance=task)
    if form.is_valid():
        print("POST data received:", request.POST)  # Debug print
        print("Title:", request.POST.get('title'))
        print("Task:", request.POST.get('task'))
        form.save()
        return redirect('index')
    else:
        form = TaskForm(instance=task)
    context = {'task': task, 'form': form}
    return render(request, "update.html", context)
