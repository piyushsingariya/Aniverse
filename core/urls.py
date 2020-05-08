from django.urls import path
from .views import IndexView, ItemDetailView

app_name = 'core'
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('anime/<pk>', ItemDetailView.as_view(), name="anime")
]