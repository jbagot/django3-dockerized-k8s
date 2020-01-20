from datetime import datetime

from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from api.models import Animal, AnimalType
from api.serializers import AnimalSerializer, AnimalTypeSerializer


class PingView(APIView):
    def get(self, request):
        return Response({'date': datetime.now()})


class AnimalsViewset(ListModelMixin, GenericViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class AnimalTypesViewset(ListModelMixin, GenericViewSet):
    queryset = AnimalType.objects.all()
    serializer_class = AnimalTypeSerializer
