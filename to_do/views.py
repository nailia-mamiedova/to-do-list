from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic, View

from .models import Task, Tag


def home_page(request):
    tasks_list = Task.objects.all().prefetch_related("tags").order_by('is_done', '-datetime')
    return render(request, "to_do/home_page.html", {"tasks_list": tasks_list})


class TaskCreateView(generic.CreateView):
    model = Task
    fields = ["content", "deadline", "tags"]
    success_url = reverse_lazy("to_do:home-page")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = ["content", "deadline", "tags"]
    success_url = reverse_lazy("to_do:home-page")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("to_do:home-page")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to_do:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to_do:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("to_do:tag-list")


class CompleteUndoTask(View):
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        task.is_done = not task.is_done
        task.save()
        return HttpResponseRedirect(
            reverse_lazy("to_do:home-page")
        )
