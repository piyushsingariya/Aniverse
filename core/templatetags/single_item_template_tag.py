from core.models import Item
from django import template

register = template.Library()

def image_count():
    if Item.media:
        qs = Item.media.objects.filter(is_video=False)
        if qs.exists():
            return qs[0].items.count()
    return -1