from django.urls import path, include


urlpatterns = [
    path('tracks/', include('api.v1.track.urls')),
    path('albums/', include('api.v1.album.urls')),
]
