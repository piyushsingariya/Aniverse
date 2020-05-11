from django.db import models
from django.shortcuts import reverse
from multiselectfield import MultiSelectField
import datetime
from sorl.thumbnail import ImageField, get_thumbnail

AUDIO_CHOICES = (
    ('Dual Audio', 'Dual Audio'),
    ('Subbed', 'Subbed'),
    ('Dubbed', 'Dubbed'),
)

GENRES_CHOICES = (
    ('Action', 'Action'),
    ('Adventure', 'Adventure'),
    ('Comedy', 'Comedy'),
    ('Drama', 'Drama'),
    ('Slice of Life', 'Slice of Life'),
    ('Fantasy', 'Fantasy'),
    ('Magic', 'Magic'),
    ('Supernatural', 'Supernatural'),
    ('Horror', 'Horror'),
    ('Mystery', 'Mystery'),
    ('Psychological', 'Psychological'),
    ('Romance', 'Romance'),
    ('Sci-Fi', 'Sci-Fi')
)

SUB_GENRES_CHOICES = (
    ('Cyberpunk', 'Cyberpunk'),
    ('Game', 'Game'),
    ('Ecchi', 'Ecchi'),
    ('Demons', 'Demons'),
    ('Harem', 'Harem'),
    ('Josei', 'Josei'),
    ('Martial Arts', 'Martial Arts'),
    ('Kids', 'Kids'),
    ('Historical', 'Historical'),
    ('Hentai', 'Hentai'),
    ('Isekai', 'Isekai'),
    ('Military', 'Military'),
    ('Mecha', 'Mecha'),
    ('Music', 'Music'),
    ('Parody', 'Parody'),
    ('Police', 'Police'),
    ('Post-Apocalyptic', 'Post-Apocalyptic'),
    ('Reverse Harem', 'Reverse Harem'),
    ('School', 'School'),
    ('Seinen', 'Seinen'),
    ('Shoujo', 'Shoujo'),
    ('Shoujo-ai', 'Shoujo-ai'),
    ('Shounen', 'Shounen'),
    ('Shounen-ai', 'Shounen-ai'),
    ('Space', 'Space'),
    ('Sports', 'Sports'),
    ('Super Power', 'Super Power'),
    ('Tragedy', 'Tragedy'),
    ('Vampire', 'Vampire'),
    ('Yuri', 'Yuri'),
    ('Yaoi', 'Yaoi')
)

DEFAULT_DESCRIPTION = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""


def year_choices():
    return [(r, r) for r in range(1984, datetime.date.today().year + 1)]


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

    class Meta:
        verbose_name_plural = "Media Attachments"


class AnimeCategory(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "Anime Categories"


class InsightDetails(models.Model):
    title = models.CharField(max_length=100)
    production_house = models.CharField(max_length=50)
    writers = models.CharField(max_length=50)
    director = models.CharField(max_length=50, blank=True, null=True)
    total_episodes = models.IntegerField(default=25)
    season_number = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Insight Details"


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
    background_image = models.ImageField(blank=True, null=True)
    description = models.TextField(default=DEFAULT_DESCRIPTION)
    rating = models.FloatField(default=7.0)
    votes = models.IntegerField(default=1000)
    ongoing = models.BooleanField(default=True)
    editors_pick = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    genres = MultiSelectField(choices=GENRES_CHOICES)
    sub_genres = MultiSelectField(choices=SUB_GENRES_CHOICES)
    year_released = models.IntegerField(choices=year_choices(), default=current_year() - 4)
    media = models.ManyToManyField(MediaAttachments, blank=True)
    insights = models.ForeignKey(InsightDetails, blank=True, on_delete=models.CASCADE)
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


class MovieItem(models.Model):
    title = models.CharField(max_length=100)
    title_english = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(default=None)
    background_image = models.ImageField(blank=True, null=True)
    description = models.TextField(default=DEFAULT_DESCRIPTION)
    rating = models.FloatField(default=7.0)
    votes = models.IntegerField(default=1000)
    editors_pick = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    genres = MultiSelectField(choices=GENRES_CHOICES)
    sub_genres = MultiSelectField(choices=SUB_GENRES_CHOICES)
    year_released = models.IntegerField(choices=year_choices(), default=current_year() - 4)
    media = models.ManyToManyField(MediaAttachments, blank=True)
    insights = models.ForeignKey(InsightDetails, blank=True, on_delete=models.CASCADE)
    characters = models.ManyToManyField(Characters, blank=True)
    language = models.CharField(choices=AUDIO_CHOICES, max_length=30, default='Subbed')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Anime Movies'

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
