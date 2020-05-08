from django.db import models
from django.shortcuts import reverse
import datetime
AUDIO_CHOICES = (
    ('Dual Audio', 'Dual Audio'),
    ('Subbed', 'Subbed'),
    ('Dubbed', 'Dubbed'),
)

def year_choices():
    return [(r, r) for r in range(1984, datetime.date.today().year+1)]
def current_year():
    return datetime.date.today().year

class MediaAttachments(models.Model):
    image = models.ImageField()
    is_video = models.BooleanField()
    video_url = models.URLField(blank=True, null=True)
    added_date = models.DateTimeField(auto_now=True)
    characters = models.ManyToManyField('Characters', blank=True)
    def __str__(self):
        return self.image.name

class AnimeCategory(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

class Characters(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    role = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Characters'

class Item(models.Model):
    title = models.CharField(max_length=100)
    title_english = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(default=None)
    description = models.TextField(blank=True, null=True)
    rating = models.FloatField(default=7.0)
    ongoing = models.BooleanField(default=True)
    genre = models.ManyToManyField(AnimeCategory)
    updated = models.DateTimeField(auto_now=True)
    year_released = models.IntegerField(choices=year_choices(), default=current_year()-4)
    media = models.ManyToManyField(MediaAttachments, blank=True)
    characters = models.ManyToManyField(Characters, blank=True)
    language = models.CharField(choices=AUDIO_CHOICES, max_length=30, default='Subbed')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Anime'
    def get_absolute_url(self):
        return reverse("core:anime", kwargs={
            'pk': self.id
        })
    def media_qs(self):
        return self.media.order_by('-added_date')[:4]
    def get_image_count(self):
        return self.media.filter(is_video=False).count()
    def get_video_count(self):
        return self.media.filter(is_video=True).count()
