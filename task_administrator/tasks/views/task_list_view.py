from rest_framework import generics
from tasks.models.task import Task
from tasks.serializers.task_serializer import  TaskSerializer

class TaskListAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer
    def get_queryset(self):
        return Task.objects.all()
