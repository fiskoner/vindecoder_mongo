from rest_framework import serializers
from vindecoder.models import Car
from rest_framework_mongoengine.serializers import DocumentSerializer


class CarSerializer(DocumentSerializer):
    class Meta:
        model = Car
        # fields = ('wmi')
        fields = '__all__'