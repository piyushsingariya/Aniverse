from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import (Item,
                     AnimeCategory,
                     MediaAttachments,
                     Character,
                     CharacterSet,
                     InsightDetails,
                     MovieItem,
                     VideoItems,
                     Request)


def linkify(field_name):
    """
    Converts a foreign key value into clickable links.

    If field_name is 'parent', link text will be str(obj.parent)
    Link will be admin url for the admin url for obj.parent.id:change
    """

    def _linkify(obj):
        app_label = obj._meta.app_label
        linked_obj = getattr(obj, field_name)
        model_name = linked_obj._meta.model_name
        view_name = f"admin:{app_label}_{model_name}_change"
        link_url = reverse(view_name, args=[linked_obj.id])
        return format_html('<a href="{}">{}</a>', link_url, linked_obj)

    _linkify.short_description = field_name  # Sets column name
    return _linkify


def make_them_completed(modeladmin, request, queryset):
    queryset.update(ongoing=False)


def request_accepted(modeladmin, request, queryset):
    queryset.update(request_accepted=True)


def duplicate_event(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()


def editors_pick(modeladmin, request, queryset):
    queryset.update(editors_pick=True)


def false_editors_pick(modeladmin, request, queryset):
    queryset.update(editors_pick=False)


make_them_completed.short_description = 'Update ongoing anime into completed'
editors_pick.short_description = 'Make Editors Pick into True'
false_editors_pick.short_description = 'Make Editors Pick into False'
duplicate_event.short_description = "Duplicate selected record"
request_accepted.short_description = "Request is accepted"


class ItemAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'rating',
                    'ongoing',
                    'editors_pick',
                    'updated',
                    'year_released',
                    linkify(field_name='character_set'),
                    'language']
    search_fields = ['title',
                     'title_english',
                     ]
    actions = [make_them_completed,
               editors_pick,
               false_editors_pick,
               duplicate_event]


class MovieItemAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'rating',
                    'editors_pick',
                    'created',
                    'updated',
                    'year_released',
                    'language']
    search_fields = ['title',
                     'title_english',
                     ]

    actions = [editors_pick,
               false_editors_pick,
               ]


class RequestAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'name',
                    'email_address',
                    'season',
                    'choice',
                    'request_accepted',
                    'message'
                    ]
    actions = [request_accepted,
               ]


admin.site.register(Item, ItemAdmin)
admin.site.register(MovieItem, MovieItemAdmin)
admin.site.register(AnimeCategory)
admin.site.register(MediaAttachments)
admin.site.register(Character)
admin.site.register(CharacterSet)
admin.site.register(InsightDetails)
admin.site.register(VideoItems)
admin.site.register(Request, RequestAdmin)
