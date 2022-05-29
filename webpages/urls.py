from django.urls import path

from webpages import views

urlpatterns = [
    path("", views.index),
    path("watch", views.watch_redirect),
    path("watch/", views.watch_redirect),
    path("watch/<int:video_id>/", views.watch),
    path("watch/<int:video_id>", views.watch),
    path("blogger_cabinet/", views.blogger_cabinet),
    path("blogger_cabinet", views.blogger_cabinet),
    path("advertiser_cabinet", views.advertiser_cabinet),
    path("advertiser_cabinet/", views.advertiser_cabinet),
    path("marketplace/", views.marketplace),
    path("marketplace", views.marketplace),
]
