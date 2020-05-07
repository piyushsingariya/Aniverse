from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Item


# def index(request):
#     return render(request, "index.html")
class IndexView(ListView):
    model = Item
    template_name = 'index.html'