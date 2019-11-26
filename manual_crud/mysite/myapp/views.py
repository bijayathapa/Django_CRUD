from django.http import HttpResponse
from django.shortcuts import render, redirect
from .book import Book
from myapp.database import Database

# Create your views here.

def index(request):
	books = Database().getBooks()
	#print(books)

	context = {
		'books':books,
	}

	return render(request, 'myapp/index.html',context)

def all(request):
    books = Database().getBooks()
    # print(len(persons))
    context = {
        'books': books,
    }
    return render(request, 'myapp/index.html', context)

def getBook(request, id):
	book = Database().getBook(id)
	return HttpResponse(book)

def insert(request):
	if request.method == 'POST':
		book_name = request.POST.get('txt_name')
		book_genre = request.POST.get('txt_genre')
		book_writer = request.POST.get('txt_writer')
		book_rating = request.POST.get('txt_rating')

		book = Book()

		book.setBookName(book_name)
		book.setBookGenre(book_genre)
		book.setBookWriter(book_writer)
		book.setBookRating(book_rating)

		db = Database()
		db.insertBook(book)
		return redirect('all')

	else:
		return render(request, 'myapp/insert_form.html')

def getBookUpdate(request):
	id = request.GET.get('id')
	book = Database().getBook(id)
	print(book)
	context = {
		'id':int(book.getId()),
		'book_name':book.getBookName(),
		'book_genre':book.getBookGenre(),
		'book_writer':book.getBookWriter(),
		'book_rating':book.getBookRating(),
	}
	return render(request, 'myapp/update_form.html',context)

def updateBook(request):
	if request.method == 'POST':
		book_name = request.POST.get('txt_name')
		book_genre = request.POST.get('txt_genre')
		book_writer = request.POST.get('txt_writer')
		book_rating = request.POST.get('txt_rating')

		book = Book()

		book.setBookName(book_name)
		book.setBookGenre(book_genre)
		book.setBookWriter(book_writer)
		book.setBookRating(book_rating)
		db = Database()
		db.updateBook(book)
		print(book)
		return redirect('all')
		#return HttpResponse(result)

def deleteBook(request, id):
	book = Database().getBook(id)
	result = Database().delete(book)
	return redirect('all')
	#return HttpResponse(result)





