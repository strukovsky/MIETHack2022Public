from rest_framework.serializers import ModelSerializer
from .models import Video, Advertiser, Blogger, Comment, Advertisement


class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"


class ContractSerializer(ModelSerializer):
    class Meta:
        model = Advertisement
        fields = "__all__"


class BloggerSerializer(ModelSerializer):
    class Meta:
        model = Blogger
        fields = "__all__"


class AdvertiserSerializer(ModelSerializer):
    class Meta:
        model = Advertiser
        fields = "__all__"

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"