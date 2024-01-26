from rest_framework import serializers
from soapservice.models import Person

class Personerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['inn', 'last_name', 'surname', 'birthdate','passport_ser','passport_num']