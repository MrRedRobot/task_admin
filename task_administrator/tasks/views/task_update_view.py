from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from tasks.models.task import Task
from tasks.serializers.task_serializer import  TaskSerializer

class TaskUpdateAPIView(generics.UpdateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self,pk):
        return self.serializer_class.Meta.model.objects.all().filter(pk=pk).first()

    def patch(self,request,pk=None):
        task = self.get_queryset(pk=pk)
        #validation
        if task:
            task_serializer = self.serializer_class(task)
            return Response(task_serializer.data, status = status.HTTP_200_OK)
        return Response({'message':'TAREA NO ENCONTRADA!'},status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        task = self.get_queryset(pk=pk)
        #validation
        if task:
            task_serializer = self.serializer_class(task, data= request.data)
            if task_serializer.is_valid():
                task_serializer.save()
                return Response(task_serializer.data, status = status.HTTP_200_OK)
            return Response(task_serializer.errors,status = status.HTTP_400_BAD_REQUEST)

