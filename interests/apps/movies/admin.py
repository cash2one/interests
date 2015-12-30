from django.contrib import admin
from apps.movies.models import (
    DouBanMovie,
)


class DouBanMovieAdmin(admin.ModelAdmin):
    list_display = ('movie_id', 'title', 'original_title', 'aka',
                    'average', 'ratings_count', 'subtype', 'directors',
                    'year', 'languages', 'genres', 'countries', 'summary')


admin.site.register(DouBanMovie, DouBanMovieAdmin)