from django.db import models


class TrackManager(models.Manager):
    def current_version_track(self):
        return None