from rest_framework import generics
from .models import Photo
from .serializers import PhotoSerializer


class ListPhoto(generics.ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class DetailPhoto(generics.RetrieveAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer