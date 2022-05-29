from django.contrib import admin
from .models import Advertiser, Video, Blogger, Comment, PlatformAction, PlatformUser, Advertisement, TransactorParams


# Register your models here.

class ContractInline(admin.StackedInline):
    model = Advertisement


class VideoInline(admin.StackedInline):
    model = Video


class CommentInline(admin.StackedInline):
    model = Comment


@admin.register(Advertiser)
class AdvertiserAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    inlines = [ContractInline]


@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    inlines = [ContractInline, VideoInline]


# admin.site.register(Advertiser)
# admin.site.register(Blogger)
admin.site.register(Advertisement)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(PlatformUser)
admin.site.register(PlatformAction)
admin.site.register(TransactorParams)