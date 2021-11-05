from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico, Endereco

class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = ("linha1", "linha2", "cidade", "estado", "pais", "latitude", "longitude")

class PontoTuristicoSerializer(ModelSerializer):
    endereco = EnderecoSerializer()
    class Meta:
        model = PontoTuristico
        fields = '__all__'