from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.

def index(request):
	movies = Movie.objects.values_list()

	context = {
		'movies':movies
	}

	return render(request,'myapp/index.html',context)

def all(request):
	movies = Movie.objects.values_list()

	context = {
		'movies':movies
	}

	return render(request,'myapp/index.html',context)

def insert(request):
	if request.method == 'POST':
		movie_name = request.POST.get('txt_name')
		movie_genre = request.POST.get('txt_genre')
		movie_director = request.POST.get('txt_director')
		movie_rating = request.POST.get('txt_rating')

		movie = Movie()

		movie.movie_name = movie_name
		movie.movie_genre = movie_genre
		movie.movie_director = movie_director
		movie.movie_rating = movie_rating

		movie.save()
		return redirect('all')
	else:
		return render(request,'myapp/insert_form.html')

def search_update(request):
	if request.method == 'GET':
		id_search = request.GET.get('id')
		movie = Movie.objects.get(id = id_search)
		context = {
			'movie':movie
		}

		return render(request,'myapp/update_form.html',context)

def update(request):
	if request.method == 'POST':
		id_search = request.POST.get('txt_id')
		movie = Movie.objects.get(id = id_search)

		movie.movie_name = request.POST.get('txt_name')
		movie.movie_genre = request.POST.get('txt_genre')
		movie.movie_director = request.POST.get('txt_director')
		movie.movie_rating = request.POST.get('txt_rating')

		movie.save()

		return redirect('all') 
	return redirect('all')

def delete(request,id):
	movie = Movie.objects.get(id = id)
	movie.delete()
	return redirect('all')
	











