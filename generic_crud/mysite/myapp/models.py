from django.db import models

# Create your models here.

class Movie(models.Model):
	id = models.AutoField(primary_key = True)
	movie_name = models.CharField(max_length = 50)
	movie_genre = models.CharField(max_length = 50)
	movie_director = models.CharField(max_length = 50)
	movie_rating = models.IntegerField(max_length = 1)

	def __str__(self):
		return (str(self.id)+", "+str(self.movie_name)+", "+str(self.movie_genre)+", "+str(self.movie_director)+", "+str(self.movie_rating))