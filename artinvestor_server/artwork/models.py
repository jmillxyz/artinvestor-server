from django.db import models

class Artwork(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(
        'artists.Artist',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
    )
    photo = models.ImageField(upload_to='media')
