from django.db import models
from django.template.defaultfilters import slugify


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
    photo = models.ImageField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)

        super(Artwork, self).save(*args, **kwargs)
