from rest_framework import permissions, viewsets
from soapservice.models import Person
from restservice.serializers import Personerializer
import logging

logging.basicConfig(level=logging.DEBUG)

class PersonModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Person.objects.all()
    serializer_class = Personerializer
    permission_classes = [permissions.AllowAny]
