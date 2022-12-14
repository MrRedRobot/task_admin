from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from tasks.models.task import Task
from tasks.serializers.task_serializer import  TaskSerializer

class TaskRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TaskSerializer

    def get(self,request,pk=None):
        task = Task.objects.filter(id = pk).first()
        if task:
            task_serializer = TaskSerializer(task)
            return Response(task_serializer.data, status = status.HTTP_200_OK)
        return Response({'message':'TAREA NO ENCONTRADA!'},status = status.HTTP_400_BAD_REQUEST)