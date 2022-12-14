from rest_framework import generics, permissions
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend


from tasks.models.task import Task
from tasks.serializers.task_serializer import  TaskSerializer

class TaskFilter(filters.FilterSet):

    STATE_CHOICES = (
    ('BACKLOG', 'Backlog'),
    ('TO DO', 'To Do'),
    ('DOING', 'Doing'),
    ('TEST', 'Test'),
    ('DONE', 'Done'),
    )
    filterName = filters.CharFilter(
        field_name='name',
        lookup_expr='exact',
        label='Nombre de la tarea'
    )
    filterDate = filters.DateFromToRangeFilter(
        field_name='delivery_date',
        lookup_expr='exact',
        label='fecha de entrega'
    )
    filterState = filters.ChoiceFilter(
        choices=STATE_CHOICES,
        field_name='state',
        lookup_expr='exact',
        label='Estado'
    )


class TaskListAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter

    def get_queryset(self):
        return Task.objects.all()
