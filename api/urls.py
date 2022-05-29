from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import VideoViewSet, ContractViewSet, BloggerViewSet, AdvertiserViewSet, CommentViewSet, UserAction

router = DefaultRouter()

router.register("videos", VideoViewSet)
router.register("contracts", ContractViewSet)
router.register("bloggers", BloggerViewSet)
router.register("advertisers", AdvertiserViewSet)
router.register("comments", CommentViewSet)

urlpatterns = [
    path("user_action/", UserAction.as_view(), name="user_action")
]
urlpatterns += router.urls
