
from rest_framework import viewsets

from Apps.Crud.models import productoModelo
from Apps.Crud.serializers import productoSerialize

class productoView(viewsets.ModelViewSet):
    queryset = productoModelo.objects.all()
    serializer_class = productoSerialize



