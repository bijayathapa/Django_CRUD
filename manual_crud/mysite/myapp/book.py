class Book():
	def __init__(self):
		self.id = 0
		self.book_name = ""
		self.book_genre = ""
		self.book_writer = ""
		self.book_rating = 0

	def getId(self):
		return (self.id)

	def getBookName(self):
		return(self.book_name)

	def getBookGenre(self):
		return(self.book_genre)

	def getBookWriter(self):
		return(self.book_writer)

	def getBookRating(self):
		return(self.book_rating)

	def setId(self, id):
		self.id = id

	def setBookName(self, book_name):
		self.book_name = book_name

	def setBookGenre(self, book_genre):
		self.book_genre = book_genre

	def setBookWriter(self, book_writer):
		self.book_writer = book_writer

	def setBookRating(self, book_rating):
		self.book_rating = book_rating


	def __str__(self):
		return str(self.id)+" | "+str(self.book_name)+" | "+str(self.book_genre)+" | "+str(self.book_writer)+" | "+str(self.book_rating)