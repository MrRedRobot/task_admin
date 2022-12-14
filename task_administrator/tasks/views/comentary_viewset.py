from rest_framework import viewsets, permissions
from tasks.models.comentary import Comentary
from tasks.serializers.comentary_serializer import ComentarySerializer

class ComentaryViewSet(viewsets.ModelViewSet):
    queryset = Comentary.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = ComentarySerializer