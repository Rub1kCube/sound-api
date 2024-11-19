from django.db import models

from apps.album.choices import AlbumTypeChoices

class Album(models.Model):
    title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    is_published = models.BooleanField(
        default=False
    )
    is_deleted = models.BooleanField(
        default=False
    )

    create_at = models.DateTimeField(
        auto_now_add=True
    )
    update_at = models.DateTimeField(
        auto_now=True
    )

    type_album = models.CharField(
        choices=AlbumTypeChoices,
        default=AlbumTypeChoices.SINGLE
    )

    file_image = models.ImageField(
        upload_to='albums',
        null=True,
        blank=True
    )
