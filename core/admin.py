from django.contrib import admin
from .models import Item, AnimeCategory, MediaAttachments, Characters


admin.site.register(Item)
admin.site.register(AnimeCategory)
admin.site.register(MediaAttachments)
admin.site.register(Characters)
