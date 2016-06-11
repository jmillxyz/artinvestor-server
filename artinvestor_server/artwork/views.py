from django.shortcuts import render
from rest_framework import generics

class ArtworkList(generics.ListAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
