from django.db import models
from django.template.defaultfilters import slugify


class Artist(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)

        super(Artist, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
