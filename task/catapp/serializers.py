from rest_framework import serializers
from .models import Catmodel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catmodel
        fields = '__all__'
