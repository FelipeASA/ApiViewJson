from django.urls import path, include

from Apps.ConsumoJson.views import *

urlpatterns= [
	path('', productosApi.as_view(), name="productosApi"),

]