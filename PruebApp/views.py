from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Inscritos
from .serializers import InscritoSerial
from django.http import JsonResponse
from rest_framework.views import APIView
from django.http import Http404

def index(request):
    return render(request, 'index.html')


#FUNCTION BASED VIEW
@api_view(['GET', 'POST'])
def participante_list(request):
    if request.method == 'GET':
        inscritos = Inscritos.objects.all()
        serial = InscritoSerial(inscritos, many=True)
        return Response(serial.data)

    if request.method == 'POST':
        serial = InscritoSerial(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def participante_detalle(request, id):
    try:
        inscritos = Inscritos.objects.get(pk=id)
    except Inscritos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = InscritoSerial(inscritos)
        return Response(serial.data)
    
    if request.method == 'PUT':
        serial = InscritoSerial(inscritos, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        inscritos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
def ver_inscritos(request):
    inscritos = Inscritos.objects.all()
    data = {'inscrito' : list(inscritos.values())}

    return JsonResponse(data)

#CLASS BASED VIEW

class ver_participantes(APIView):
    def get(self, request):
        inscritos=Inscritos.objects.all()
        serial = InscritoSerial(inscritos, many=True)
        return Response(serial.data)
    
    def post(self, request):
        serial = InscritoSerial(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class ver_detalle(APIView):
    def get_object(self, pk):
        try:
            return Inscritos.objects.get(pk=pk)
        except Inscritos.DoesNotExist:
            return Http404

    def get(self, request, pk):
        inscritos = self.get_object(pk)
        serial = InscritoSerial(inscritos)
        return Response(serial.data)

    def put(self, request, pk):
        inscritos = self.get_object(pk)
        serial = InscritoSerial(inscritos, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.data, status=status.HTTP_400_BAD_REQUEST)  
    
    def delete(self, request, pk):
        inscritos = self.get_object(pk)
        inscritos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



