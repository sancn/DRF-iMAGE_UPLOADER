
from rest_framework.response import Response  
from rest_framework import status
from rest_framework import viewsets
from .models import UploadedImage
from imageApp.serializers import UploadSerializer

class UploadViewset(viewsets.ViewSet):
  serializer_class = UploadSerializer
  queryset=UploadedImage.objects.all()

  def create(self,request):
    serializer=self.serializer_class(data=self.request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data,status=status.HTTP_201_CREATED)
  