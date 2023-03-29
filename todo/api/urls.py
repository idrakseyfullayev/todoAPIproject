from django.urls import path
from todo.api import views




urlpatterns = [
    path('todos/', views.TodoModelListAPIview.as_view(), name="todos"),
    path('todo-create/', views.TodoModelCreateAPIView.as_view(), name="todo-create"),
    path('todo-update/<int:id>/', views.TodoModelUpdateAPIView.as_view(), name="todo-update"),
    path('todo-destroy/<int:id>/', views.TodoModelDestroyAPIView.as_view(), name="todo-destroy"),
]




