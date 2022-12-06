from rest_framework import viewsets, permissions
from tasks.models.task import Task
from tasks.serializers.task_serializer import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = TaskSerializer

