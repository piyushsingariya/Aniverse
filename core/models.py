from django.db import models

AUDIO_CHOICES = (
    ('Dual Audio', 'Dual Audio'),
    ('Subbed', 'Subbed'),
    ('Dubbed', 'Dubbed'),
)
class AnimeCategory(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

class Item(models.Model):
    title = models.CharField(max_length=100)
    title_english = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(default=None)
    description = models.TextField(blank=True, null=True)
    rating = models.FloatField(default=7.0)
    ongoing = models.BooleanField(default=True)
    genre = models.ManyToManyField(AnimeCategory)
    updated = models.DateTimeField(auto_now=True)

    language = models.CharField(choices=AUDIO_CHOICES, max_length=30, default='Subbed')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Anime'