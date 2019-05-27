from django.shortcuts import render
from django.http import HttpResponse
import json

from Apps.Crud.models import productoModelo
from Apps.Crud.serializers import productoSerialize
from rest_framework.views import APIView

# Create your views here.
class productosApi(APIView):

    serializers = productoSerialize
    def get(self, request, format=None):
        

        datos = productoModelo.objects.all()
        response_data = self.serializers(datos, many=True)
        response_json = json.dumps(response_data.data)
        return HttpResponse(response_json, content_type='application/json')