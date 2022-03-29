from empresa.models import empresa
from rest_framework import serializers

class empresa_serializer(serializers.ModelSerializer):
    class Meta:
        model = empresa
        fields = ('id', 'direccion', 'nombreEmpresa','telefonoEmpresa','nit')
