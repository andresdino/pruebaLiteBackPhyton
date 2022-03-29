from empresa.serializers import empresa_serializer
from empresa.models import empresa

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def crear_empresa(request):
    if request.method == 'POST':
        crear = empresa_serializer(data = request.data)
        if crear.is_valid():
            crear.save()
            return Response({"mensaje":"Registro creado de manera exitosa", "data":crear.data} , status = status.HTTP_201_CREATED)
        return Response(crear.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def actualizar_empresa(request, id):
    if request.method == 'PUT':
        actualizar = empresa.objects.get(id = id)
        serializer = empresa_serializer(actualizar, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje":"Se actualizo correctamente..", "data": serializer.data}, status = status.HTTP_200_OK)
        return Response({"mensaje":"Hemos tenido un error, intenta mas tarde", "error":serializer.errors}, status = status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def eliminar_empresa(request,id):
    if request.method == 'DELETE':
        try:
            eliminar = empresa.objects.get(id = id)
            eliminar.delete()
            return Response({"mensaje":"Registro eliminado"}, status = status.HTTP_200_OK)
        except:
            return Response({"mensaje":"Error al eliminar el registro en la base de datos, intenta mas tarde"}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listar_empresas(request):
    if request.method == 'GET':
        modelo_empresa = empresa.objects.all()
        obtener_empresas = empresa_serializer(modelo_empresa, many=True)
        return Response({"mensaje":"Consulta exitosa", "data":obtener_empresas.data}, status = status.HTTP_200_OK)




