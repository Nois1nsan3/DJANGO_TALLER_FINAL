from rest_framework import serializers
from .models import Inscritos

class InscritoSerial(serializers.ModelSerializer):
    class Meta:
        model = Inscritos
        fields = '__all__'