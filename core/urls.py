from django.urls import path
from .views import (IndexView,
                    ItemDetailView,
                    AnimeListingView,
                    Search,
                    AnimeGridingView,
                    MovieDetailView,
                    MovieGridingView,
                    testing)

app_name = 'core'
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('anime/<pk>/', ItemDetailView.as_view(), name="anime"),
    path('movie/<pk>/', MovieDetailView.as_view(), name="movie"),
    path('anime_all/list/', AnimeListingView.as_view(), name="anime-listing"),
    path('anime_all/grid/', AnimeGridingView.as_view(), name="anime-griding"),
    path('movie_all/grid/', MovieGridingView.as_view(), name="movie-griding"),
    path('search/anime/', Search.as_view(), name="search"),
    path('testing/', testing, name="testing"),

]