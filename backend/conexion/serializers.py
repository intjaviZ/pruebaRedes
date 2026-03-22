from rest_framework import serializers

class SalaDetalleSerializer(serializers.Serializer):
    id_sala = serializers.CharField(max_length=4)
    jugadores = serializers.IntegerField()
    tipo = serializers.CharField(allow_blank=True)
    lleno = serializers.BooleanField()

class StateSerializer(serializers.Serializer):
    # DictField le dice a DRF: "Espera un mapa donde las llaves son Strings 
    # y los valores deben cumplir con SalaDetalleSerializer"
    salas = serializers.DictField(
        child=SalaDetalleSerializer(),
        read_only=True
    )