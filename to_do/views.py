from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Task


def home_page(request):
    tasks_list = Task.objects.all().prefetch_related("tags")
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
