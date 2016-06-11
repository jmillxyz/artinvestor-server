from rest_framework import serializers
from artist.models import Artist
from users.models import User
from .models import Artwork


class ArtworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artwork
        fields = ('name', 'artist', 'user', 'photo')
