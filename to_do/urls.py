from django.urls import path
from .views import home_page, TaskCreateView, TaskUpdateView, TaskDeleteView


urlpatterns = [
    path("", home_page, name="home-page"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="update-task"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="delete-task"),
]


app_name = "to_do"
