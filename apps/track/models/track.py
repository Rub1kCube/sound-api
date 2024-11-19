from django.db import models

from apps.track.choices import GenresChoices
from apps.track.managers import TrackManager
from utils.models.base import BaseModel


class Track(BaseModel):
    objects = TrackManager()

    track_version = models.ForeignKey(
        'TrackVersion',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )


class TrackVersion(BaseModel):
    title = models.CharField(
        max_length=155,
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    text = models.TextField(
        null=True,
        blank=True,
    )
    duration = models.CharField(
        max_length=10,
        null=False,
        blank=False,
    )
    is_explicit_content = models.BooleanField(
        default=False,
    )
    upload_date = models.DateTimeField(
        auto_now_add=True,
    )
    edit_date = models.DateTimeField(
        auto_now=True,
    )
    order = models.PositiveSmallIntegerField(
        default=0,
        null=False
    )

    genre = models.CharField(
        choices=GenresChoices,
        default=GenresChoices.OTHER,
    )

    album = models.OneToOneField(
        'Album',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    file_track = models.ForeignKey(
        'TrackFile',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        class_name = self.__class__.__name__
        return (f'<{class_name}> {self.id=}, {self.title!r} | '
                f'possible to publish: {bool(self.file_track and not self.file_track)} | '
                f'{self.genre=}')


class TrackFile(BaseModel):
    file = models.FileField(
        upload_to='tracks'
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )


    def __str__(self):
        return f"<{self.__class__.__name__} {self.id=}, {self.file=}, {self.uploaded_at=}>"

