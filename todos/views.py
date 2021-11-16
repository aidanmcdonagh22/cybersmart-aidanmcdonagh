from django.views.generic.list import ListView
from .models import Todo
from rest_framework.generics import (
    CreateAPIView, UpdateAPIView, DestroyAPIView
)
from .serializers import TodoSerializer

class ListTodoView(ListView):
    template_name = 'todo_list.html'
    model = Todo

class AddTodoView(CreateAPIView):
    serializer_class = TodoSerializer

class UpdateTodoView(UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DeleteTodoView(DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer