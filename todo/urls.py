from django.urls import path
from .views import (TaskListView,
                    TagsListView,
                    TagsCreateView,
                    TagsUpdateView,
                    TagsDeleteView,
                    TodoCreateView, TodoUpdateView,
                    TodoDeleteView, toggle_assign_to_tag)


urlpatterns = [
    path("", TaskListView.as_view(), name="todo-list"),
    path("tags/", TagsListView.as_view(), name="tags-list"),
    path("tags/create/", TagsCreateView.as_view(),
         name="tags-create"),
    path("tags/<int:pk>/update/", TagsUpdateView.as_view(),
         name="tags-update"),
    path("tags/<int:pk>/delete/", TagsDeleteView.as_view(),
         name="tags-delete"),

    path("create/", TodoCreateView.as_view(),
         name="todo-create"),
    path("<int:pk>/update/", TodoUpdateView.as_view(),
         name="todo-update"),
    path("<int:pk>/delete/", TodoDeleteView.as_view(),
         name="todo-delete"),
    path("<int:pk>/toggle-assign/", toggle_assign_to_tag,
         name="toggle-tag-assign",
    ),
]

app_name = "todo"
