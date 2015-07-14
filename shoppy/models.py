from django.db import models


class Genres(models.Model):
	genre = models.CharField(max_length = 128, unique = True)

	def __str__(self):
		return '%s'%self.genre

class Movies(models.Model):
	popularity = models.FloatField()
	director = models.CharField(max_length = 128)
	genre = models.ManyToManyField(Genres, related_name = 'movies')
	imdb_score = models.FloatField()
	movie_name = models.CharField(max_length = 500)
