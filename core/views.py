from django.shortcuts import render
from django.views.generic import DetailView, ListView, View
from .models import Item, MovieItem, VideoItems
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain


def latest_updated_list():
    return Item.objects.order_by("-created")[:20]


def testing(request):
    return render(request, 'request-anime.html')


class Search(ListView):
    def get(self, *args, **kwargs):
        # url/?q="_____"
        # will be our search query
        queryset = Item.objects.all()
        movieset = MovieItem.objects.all()
        query = self.request.GET.get('search_item')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(title_english__icontains=query) |
                Q(description__icontains=query)
            ).distinct()
        if query:
            movieset = movieset.filter(
                Q(title__icontains=query) |
                Q(title_english__icontains=query) |
                Q(description__icontains=query)
            ).distinct()
        result_list = list(chain(queryset, movieset))
        context = {
            'results': result_list,
            'query': query
        }
        return render(self.request, 'search-grid.html', context)


class AnimeListingView(View):
    def get(self, *args, **kwargs):
        queryset = Item.objects.all()

        paginator = Paginator(queryset, 10)
        page_requested_var = 'page'
        page = self.request.GET.get(page_requested_var)
        try:
            paginated_queryset = paginator.page(page)
        except PageNotAnInteger:
            paginated_queryset = paginator.page(1)
        except EmptyPage:
            paginated_queryset = paginator.page(paginator.num_pages)
        context = {
            'object_list': queryset,
            'page_number': page_requested_var,
            'queryset': paginated_queryset
        }
        return render(self.request, 'listing.html', context)


class AnimeGridingView(View):
    def get(self, *args, **kwargs):
        queryset = Item.objects.all()

        paginator = Paginator(queryset, 30)
        page_requested_var = 'page'
        page = self.request.GET.get(page_requested_var)
        try:
            paginated_queryset = paginator.page(page)
        except PageNotAnInteger:
            paginated_queryset = paginator.page(1)
        except EmptyPage:
            paginated_queryset = paginator.page(paginator.num_pages)
        context = {
            'object_list': queryset,
            'page_number': page_requested_var,
            'queryset': paginated_queryset
        }
        return render(self.request, 'griding.html', context)


class MovieGridingView(View):
    def get(self, *args, **kwargs):
        queryset = MovieItem.objects.all()

        paginator = Paginator(queryset, 30)
        page_requested_var = 'page'
        page = self.request.GET.get(page_requested_var)
        try:
            paginated_queryset = paginator.page(page)
        except PageNotAnInteger:
            paginated_queryset = paginator.page(1)
        except EmptyPage:
            paginated_queryset = paginator.page(paginator.num_pages)
        context = {
            'object_list': queryset,
            'page_number': page_requested_var,
            'queryset': paginated_queryset
        }
        return render(self.request, 'movielisting-grid.html', context)


class IndexView(View):
    def get(self, *args, **kwargs):
        latest_updated = latest_updated_list()
        ongoing_list = Item.objects.filter(ongoing=True).order_by("-updated")
        rated_list = Item.objects.filter(ongoing=True).order_by("-rating")
        voted_list = Item.objects.filter(ongoing=True).order_by("-votes")
        editor_list = Item.objects.filter(ongoing=True, editors_pick=True)

        rated_movie_list = MovieItem.objects.order_by("-rating")
        latest_movie_list = MovieItem.objects.order_by("-created")

        videos = VideoItems.objects.filter(publish=True).order_by("-created_at")
        context = {
            'latest_list': latest_updated,
            'ongoing_list': ongoing_list,
            'rated_list': rated_list,
            'voted_list': voted_list,
            'editor_list': editor_list,
            'latest_movie_list': latest_movie_list,
            'rated_movie_list': rated_movie_list,
            'videos': videos,
        }
        return render(self.request, "index.html", context)


class ItemDetailView(DetailView):
    model = Item
    template_name = 'moviesingle.html'


class MovieDetailView(DetailView):
    model = MovieItem
    template_name = 'moviesingle.html'
