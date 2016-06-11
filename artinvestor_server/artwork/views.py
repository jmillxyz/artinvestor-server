from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, \
                                    RetrieveUpdateDestroyAPIView

from .serializers import ArtworkSerializer
from .models import Artwork


class ArtworkCreateReadView(ListCreateAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    lookup_field = 'slug'

class ArtworkReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    lookup_field = 'slug'
