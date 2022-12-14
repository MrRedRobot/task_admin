import datetime

from rest_framework import serializers
from tasks.models.task import Task
from tasks.serializers.comentary_serializer import ComentarySerializer

class TaskSerializer(serializers.ModelSerializer):
    #comentary= ComentarySerializer()
    comentary= serializers.StringRelatedField()

    class Meta:
        model = Task
        fields = ('id','name','description','state', 'priority', 'delivery_date', 'comentary',)
        #read_only_fields = ('id',)


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task

    def to_representation(self,instance):
        return {
            'id':instance['id'],
            'nombre':instance['name'],
            'descripcion':instance['description'],
            'estado': instance['state'],
            'prioridad': instance['priority'],
            'fecha de entrega':instance['delivery_date']
        }