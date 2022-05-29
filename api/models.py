from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db import models

fs = FileSystemStorage(location='./static/videos/')


class Advertiser(models.Model):
    name = models.CharField("Name", max_length=150)
    address = models.CharField("Address", max_length=42)

    def __str__(self):
        return self.name


class Blogger(models.Model):
    name = models.CharField("Name", max_length=150)
    address = models.CharField("Address", max_length=42)
    date_signed_in = models.DateField("Date signed in")

    def __str__(self):
        return self.name


class Video(models.Model):
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE, related_name="bloggers_video")
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    content_file = models.FileField(storage=fs)
    medium_time_watching = models.PositiveIntegerField(default=0)
    count_of_watches = models.IntegerField(default=0)


class PlatformUser(models.Model):
    address = models.CharField(max_length=255)
    reactions = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.address


class Comment(models.Model):
    contents = models.TextField()
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="comments_video")
    author = models.ForeignKey(PlatformUser, on_delete=models.CASCADE, related_name="comments_author")


class PlatformAction(models.Model):
    user = models.ForeignKey(PlatformUser, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=100)
    tx = models.CharField(max_length=255, blank=True, null=True, unique=True)

    def __str__(self):
        return f"{self.user} done {self.action_type}"


class Advertisement(models.Model):
    class StatusChoices(models.IntegerChoices):
        INACTIVE = 0
        ACTIVE = 1
        TAKEN = 2

    id_in_contract = models.PositiveBigIntegerField()
    desired_reactions = models.PositiveBigIntegerField()
    desired_comments = models.PositiveBigIntegerField()
    threshold_reactions = models.PositiveBigIntegerField()
    threshold_comments = models.PositiveBigIntegerField()
    tips = models.PositiveBigIntegerField()
    total_calculated_price = models.PositiveBigIntegerField()
    until = models.PositiveBigIntegerField()
    status = models.PositiveBigIntegerField(choices=StatusChoices.choices)
    actualReactions = models.PositiveBigIntegerField()
    actualComments = models.PositiveBigIntegerField()
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE, related_name="advertisers")
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE, related_name="bloggers_contract")
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="advertisements", null=True, blank=True)


class TransactorParams(models.Model):
    nonce = models.PositiveBigIntegerField(default=0)
