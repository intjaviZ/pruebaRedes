from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SalaDetalleSerializer
import string
import secrets

sala = {
    "id_sala": "",
    "jugadores": 2,
    "tipo": "",
    "lleno": False
}

state = {}

class CrearSala(APIView):
    def crearCodigo(self):
        longitud_id = 4
        caracteres = string.ascii_uppercase + string.digits
        while True:
            nuevo_id = ''.join(secrets.choice(caracteres) for _ in range(longitud_id))
            if nuevo_id not in state:
                return nuevo_id
    
    def get(self, request):
        serializer = SalaDetalleSerializer(state.values(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data.get('crear_sala')
        
        if data == 1:
            codigo = self.crearCodigo()
            state[codigo] = sala.copy()
            state[codigo]['id_sala'] = codigo
            serializer = SalaDetalleSerializer(state[codigo])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"Status": "error"}, status=status.HTTP_400_BAD_REQUEST)