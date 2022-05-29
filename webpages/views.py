import datetime
import random
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from api.models import Video, Comment, Advertisement, Blogger, Advertiser
from django.shortcuts import get_object_or_404


# Create your views here.

def index(request: HttpRequest):
    return render(request, "Index.html")


def watch_redirect(request: HttpRequest):
    video = random.choice(Video.objects.all())
    return HttpResponseRedirect(f"/watch/{video.id}/")


def watch(request: HttpRequest, video_id: int):
    if video_id == -1:
        video = random.choice(Video.objects.all())
    else:
        video = get_object_or_404(Video, id=video_id)
    return render(request, "Watch.html", context={
        "video": f"videos/{video.content_file.name}",
        "video_id": video.id,
        "likes": video.likes,
        "dislikes": video.dislikes,
        "comments": Comment.objects.filter(video=video)
    })


def blogger_cabinet(request: HttpRequest):
    advertisement = Advertisement.objects.get(blogger__address=Blogger.objects.first().address,
                                              status=Advertisement.StatusChoices.ACTIVE)
    deadline = datetime.datetime.fromtimestamp(advertisement.until).strftime("%d %B %H:%M")
    return render(request, "BloggerCabinet.html", context={
        "advertisement": advertisement,
        "blogger": Blogger.objects.first(),
        "advertisement_deadline": deadline,
        "video_comments": Comment.objects.filter(video_id=advertisement.video.id).count(),
        "video_reactions": advertisement.video.likes + advertisement.video.dislikes,
    })


def advertiser_cabinet(request: HttpRequest):
    advertisement = Advertisement.objects.get(advertiser__address=Advertiser.objects.first().address)
    deadline = datetime.datetime.fromtimestamp(advertisement.until).strftime("%d %B %H:%M")
    return render(request, "AdvertiserCabinet.html", context={
        "advertisement": advertisement,
        "advertiser": Advertiser.objects.first(),
        "advertisement_deadline": deadline,
        "video_comments": Comment.objects.filter(video_id=advertisement.video.id).count()

    })


def marketplace(request: HttpRequest):
    return render(request, "Marketplace.html")
