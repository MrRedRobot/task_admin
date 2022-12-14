from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from tasks.models.task import Task
from tasks.serializers.task_serializer import  TaskSerializer

class TaskCreateAPIView(generics.CreateAPIView):
    serializer_class = TaskSerializer

    def post(self,request):
        task_serializer = self.serializer_class(data = request.data)
        #validation
        if task_serializer.is_valid():
            task_serializer.save()
            return Response({'message':'Tarea Creada Exitosamente!'}, status = status.HTTP_201_CREATED)
        return Response(task_serializer.errors,status = status.HTTP_400_BAD_REQUEST)