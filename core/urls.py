from django.urls import path
from .views import IndexView, ItemDetailView, AnimeListingView, Search

app_name = 'core'
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('anime/<pk>', ItemDetailView.as_view(), name="anime"),
    path('anime-list/all/', AnimeListingView.as_view(), name="anime-listing"),
    path('search/anime/', Search.as_view(), name="search"),
]