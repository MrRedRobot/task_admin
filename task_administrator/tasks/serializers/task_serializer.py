from rest_framework import serializers
from tasks.models.task import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name','description','state', 'priority', 'delivery_date')
        read_only_fields = ('id',)
