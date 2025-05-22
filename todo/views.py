from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
#from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from todo.models import Tag, Task
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from todo.forms import TaskForm
# Create your views here.


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "todo/task_list.html"
    paginate_by = 3


class TagsListView(generic.ListView):
    model = Tag
    context_object_name = "tags_list"
    template_name = "todo/tags_list.html"
    paginate_by = 3


class TagsCreateView(generic.CreateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("todo:tags-list")
    template_name = "todo/tags_form.html"

class TagsUpdateView(generic.UpdateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("todo:tags-list")
    template_name = "todo/tags_form.html"


class TagsDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tags-list")
    template_name = "todo/tags_confirm_delete.html"


class TodoCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:todo-list")
    template_name = "todo/todo_form.html"


class TodoUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:todo-list")
    template_name = "todo/todo_form.html"


class TodoDeleteView(generic.DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:todo-list")
    template_name = "todo/task_confirm_delete.html"


def toggle_assign_to_tag(request, pk):
    task = Task.objects.get(id=pk)

    if task.done:
        task.done = False
    else:
        task.done = True

    task.save()

    return HttpResponseRedirect(reverse_lazy("todo:todo-list"))

