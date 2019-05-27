from rest_framework import serializers
from Apps.Crud.models import productoModelo

class productoSerialize(serializers.ModelSerializer):
    class Meta:
        model = productoModelo
        fields = ['codigo', 'nombre', 'detalle', 'precio','fecha_ingreso', 'stock']