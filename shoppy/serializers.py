from shoppy.models import Movies, Genres
from rest_framework import serializers


class GenresSerializer(serializers.ModelSerializer):

	class Meta:
		model = Genres
		depth = 1
		fields = ('genre',)

class MoviesSerializer(serializers.ModelSerializer):
	#genre = serializers.CharField(max_length = 128, choices = Movies.GENRE_CHOICES)

	class Meta:
		model = Movies
		fields = ('popularity', 'director', 'imdb_score', 'genre',
						'movie_name')