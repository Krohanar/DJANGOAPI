from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from comentarios.models import Comentario
from comentarios.api.serializers import ComentarioSerializer


class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    def get_queryset(self):

        return Comentario.objects.all()