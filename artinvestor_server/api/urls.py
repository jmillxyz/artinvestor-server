# -*- coding: utf-8 -*-
from django.conf.urls import url

from artinvestor_server.artwork import views as artwork_views
from artinvestor_server.artists import views as artist_views
from artinvestor_server.users import views as user_views


urlpatterns = [
    # URL pattern for the ArtistCreateReadView
    url(
        regex=r'artists/$',
        view=artist_views.ArtistCreateReadView.as_view(),
        name='artists'
    ),

    url(
        regex=r'artists/(?P<slug>[-\w]+)/$',
        view=artist_views.ArtistReadUpdateDeleteView.as_view(),
        name='artists'
    ),

    # URL pattern for the ArtistCreateReadView
    url(
        regex=r'artwork/$',
        view=artwork_views.ArtworkCreateReadView.as_view(),
        name='artwork'
    ),

    url(
        regex=r'artwork/(?P<slug>[-\w]+)/$',
        view=artwork_views.ArtworkCreateReadView.as_view(),
        name='artists'
    ),

]
