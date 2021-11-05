from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avaliacao
from avaliacoes.api.serializers import AvaliacoesSerializer

class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacoesSerializer

    def get_queryset(self):

        return Avaliacao.objects.all()