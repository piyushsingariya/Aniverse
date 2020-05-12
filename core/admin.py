from django.contrib import admin
from .models import Item, AnimeCategory, MediaAttachments, Characters, InsightDetails, MovieItem


def make_them_completed(modeladmin, request, queryset):
    queryset.update(ongoing=False)


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


class ItemAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'rating',
                    'ongoing',
                    'editors_pick',
                    'created',
                    'updated',
                    'year_released',
                    'language']
    search_fields = ['title',
                     'title_english',
                     ]

    actions = [make_them_completed,
               editors_pick,
               false_editors_pick,
               duplicate_event]


admin.site.register(Item, ItemAdmin)
admin.site.register(MovieItem)
admin.site.register(AnimeCategory)
admin.site.register(MediaAttachments)
admin.site.register(Characters)
admin.site.register(InsightDetails)
