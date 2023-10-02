from django.shortcuts import render
from .models import Task


def home_page(request):
    tasks_list = Task.objects.all().prefetch_related("tags")
    return render(request, "to_do/home_page.html", {"tasks_list": tasks_list})
