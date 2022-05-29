from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api.blockchain import write_reactions_to_web3, write_comments_to_web3, mint_reward_to_user, get_balance_of_user
from api.models import PlatformUser, PlatformAction
from api.serializers import *


class VideoViewSet(ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
    http_method_names = ["get", "post", "head", "options"]


class ContractViewSet(ModelViewSet):
    serializer_class = ContractSerializer
    queryset = Advertisement.objects.all()
    http_method_names = ["get", "post", "head", "options"]


class BloggerViewSet(ModelViewSet):
    serializer_class = BloggerSerializer
    queryset = Blogger.objects.all()
    http_method_names = ["get", "post", "head", "options"]


class AdvertiserViewSet(ModelViewSet):
    serializer_class = AdvertiserSerializer
    queryset = Advertiser.objects.all()
    http_method_names = ["get", "post", "head", "options"]


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    http_method_names = ["get", "post", "head", "options"]


class UserAction(APIView):

    @csrf_exempt
    def post(self, request: Request):
        action_type = request.data["action_type"]
        address = request.data["address"]
        action_data = request.data["action_data"]
        video = get_object_or_404(Video, id=request.data["video"])
        user, _ = PlatformUser.objects.get_or_create(address=address)
        if action_type == "REACTION":
            user.reactions += 1
            if action_data == "LIKE":
                video.likes += 1
            elif action_data == "DISLIKE":
                video.dislikes += 1
            mint_reward_to_user(address, 10)
        elif action_type == "COMMENT":
            user.comments += 1
            Comment.objects.create(contents=action_data, video=video, author=user)
            write_comments_to_web3(video.blogger.address, 1)
            mint_reward_to_user(address, 50)
        video.save()
        PlatformAction.objects.create(user=user, action_type=action_type)
        user.save()
        return Response()

    def get(self, request: Request):
        address: str = request.query_params.get("address")
        user = get_object_or_404(PlatformUser, address=address.lower())
        return Response({
            "reactions": user.reactions,
            "comments": user.comments,
            "next_gift": 500,
            "balance": get_balance_of_user(address)
        })
