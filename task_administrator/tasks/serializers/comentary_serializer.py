from rest_framework import serializers
from tasks.models.comentary import Comentary

class ComentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentary
        fields = ('comentary_text',)
        read_only_fields = ('id',)
        verbose_name = ("Comentario")
        verbose_name_plural = ("Comentarios")