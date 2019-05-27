from rest_framework import routers 
from django.urls import path, include

from Apps.Crud.views import productoView

router = routers.DefaultRouter()
router.register('', productoView)
urlpatterns = [
    path('', include(router.urls)),
    
]
