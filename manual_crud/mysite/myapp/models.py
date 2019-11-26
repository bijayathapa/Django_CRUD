from django.db import models

# Create your models here.

class Book(models.Model):
	id = models.AutoField(primary_key = True)
	book_name = models.CharField(max_length = 50)
	book_genre = models.CharField(max_length = 30)
	book_writer = models.CharField(max_length = 50)
	book_rating = models.IntegerField(max_length = 1)


	def __str__(self):
		return str(self.id)+", "+str(self.book_name)+", "+str(self.book_genre)+", "+str(self.book_writer)+", "+str(self.book_rating)
