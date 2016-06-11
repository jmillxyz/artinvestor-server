from rest_framework.serializers import ModelSerializer

from artinvestor_server.artists.models import Artist
from artinvestor_server.users.models import User

from .models import Artwork


class ArtworkSerializer(ModelSerializer):

    class Meta:
        model = Artwork
        fields = ('id', 'name', 'artist', 'user', 'photo',)
