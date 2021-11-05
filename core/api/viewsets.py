from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico, Endereco
from core.api.serializers import PontoTuristicoSerializer, EnderecoSerializer



class PontoTuristicoViewSet(ModelViewSet):
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    search_fields = []
    filter_fields = ['id', 'endereco__linha1', 'endereco__linha2']

    def get_queryset(self):
        queryset = PontoTuristico.objects.all()
        estado = self.request.query_params.get('estado',None)
        if estado:
            queryset = PontoTuristico.objects.filter(endereco=estado)
        return queryset


class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

    def get_queryset(self):
        cidade = self.request.query_params.get('cidade', None)
        pais = self.request.query_params.get('pais', None)
        queryset = Endereco.objects.all()
        if cidade:
            queryset = Endereco.objects.filter(cidade=cidade)
        if pais:
            queryset = Endereco.objects.filter(pais=pais)

        return queryset