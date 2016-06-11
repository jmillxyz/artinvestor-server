from rest_framework import serializers
from artwork.models import Artwork
from artist.models import Artist
from users.models import User


class ArtworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artwork
        fields = ('name', 'artist', 'user', 'photo')
