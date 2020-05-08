from django.shortcuts import render
from django.views.generic import DetailView, ListView, View
from .models import Item

def latest_updated_list():
    return Item.objects.order_by("-updated")[:13]

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