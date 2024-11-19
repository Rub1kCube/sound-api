from django.db import models


class AlbumTypeChoices(models.TextChoices):
    STUDIO_ALBUM = "STUDIO_ALBUM", "Студийный альбом"
    LIVE_ALBUM = "LIVE_ALBUM", "Концертный альбом"
    COMPILATION = "COMPILATION", "Сборник"
    EP = "EP", "Мини-альбом (EP)"
    SINGLE = "SINGLE", "Сингл"
    CONCEPT_ALBUM = "CONCEPT_ALBUM", "Концептуальный альбом"
    COVER_ALBUM = "COVER_ALBUM", "Кавер-альбом"
    REMIX_ALBUM = "REMIX_ALBUM", "Альбом ремиксов"
    SOUNDTRACK = "SOUNDTRACK", "Аудио-саундтрек"
    SPECIAL_ALBUM = "SPECIAL_ALBUM", "Специальный альбом"
