from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Task
from .forms import TodoUpdateForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


class TodoListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task_list'


class TodoDetailView(DetailView):
    model = Task
    template_name = 'detailpage.html'
    context_object_name = 'task'


class TodoUpdateView(UpdateView):
    model = Task
    template_name = 'update_task_classview.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('todoapp:classbaseviewdetail', kwargs={'pk': self.object.id})


class TodoDeleteView(DeleteView):
    model = Task
    template_name = 'delete_task.html'
    success_url = reverse_lazy('todoapp:classbaseviewhome')


def homepage(request):
    task_list = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        task = Task(name=name, priority=priority,date=date)
        task.save()

    return render(request, 'home.html', {'task_list': task_list})


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete_task.html', {'task': task})


def update_task(request,task_id):
    update_task_id = Task.objects.get(id=task_id)
    update_form = TodoUpdateForm(request.POST or None, instance=update_task_id)
    if update_form.is_valid():
        update_form.save()
        return redirect('/')
    return render(request, 'update_task.html', {'update_form': update_form})

