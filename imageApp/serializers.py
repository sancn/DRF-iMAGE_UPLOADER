from rest_framework.serializers import Serializer,FileField
from .models import *
from rest_framework import serializers
class UploadSerializer(serializers.ModelSerializer):
    image_url = serializers.FileField()
    class Meta:
        model=UploadedImage
        fields= ['image_url']
