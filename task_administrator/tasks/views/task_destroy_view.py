from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from tasks.models.task import Task
from tasks.serializers.task_serializer import  TaskSerializer

class TaskDestroyAPIView(generics.DestroyAPIView):
    serializer_class = TaskSerializer

    def delete(self,request,pk=None):
        task = Task.objects.filter(id = pk).first()
        if task:
            task.delete()
            return Response({'message':'Tarea Eliminada!'},status = status.HTTP_200_OK)
        return Response({'message':'Tarea No Encontrada!'},status = status.HTTP_400_BAD_REQUEST)
