from django.shortcuts import render
from django.views.generic import DetailView, ListView, View
from .models import Item
from django.db.models import Q


def latest_updated_list():
    return Item.objects.order_by("-updated")[:13]


class Search(ListView):
    def get(self, *args, **kwargs):
        # url/?q="_____"
        # will be our search query
        queryset = Item.objects.all()
        query = self.request.GET.get('search_item')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(title_english__icontains=query) |
                Q(description__icontains=query)
            ).distinct()
        context = {
            'results': queryset,
            'query': query
        }
        return render(self.request, 'search.html', context)


class AnimeListingView(ListView):
    model = Item
    template_name = "listing.html"
    paginate_by = 1

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)


class IndexView(View):
    def get(self, *args, **kwargs):
        latest_updated = latest_updated_list()
        context = {
            'latest_list': latest_updated
        }
        return render(self.request, "index.html", context)


class ItemDetailView(DetailView):
    model = Item
    template_name = 'moviesingle.html'
