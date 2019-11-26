import sqlite3
from sqlite3 import Error

import sys

from . book import Book

class Database():

	def getBooks(self):
		books = []

		try:
			conn = sqlite3.connect('db.sqlite3')

			sql = """SELECT * FROM main.myapp_book"""

			cur = conn.cursor()
			cur.execute(sql)

			while True:
				record = cur.fetchone()
				if record == None:
					break
				else:
					books.append(record)
			conn.close()
		except Error as e:
			print(e)

		return books

	def getBook(self, id):
		book = Book()
		try:
			conn = sqlite3.connect('db.sqlite3')

			sql = """SELECT * FROM main.myapp_book WHERE id=?"""
			value = (id,)
			cur = conn.cursor()
			cur.execute(sql,value)
			while True:
				record = cur.fetchone()
				if record == None:
					break
				else:
					book.setId(record[0])
					book.setBookName(record[1])
					book.setBookGenre(record[2])
					book.setBookWriter(record[3])
					book.setBookRating(record[4])
			conn.close()
		except Error as e:
			print(e)
		return book

	def insertBook(self, book):
		try:
			conn = sqlite3.connect('db.sqlite3')
			sql = """INSERT INTO main.myapp_book(book_name, book_genre, book_writer, book_rating) VALUES(?,?,?,?)"""
			value = (book.getBookName(),book.getBookGenre(),book.getBookWriter(),book.getBookRating())

			cur = conn.cursor()
			cur.execute(sql,value)
			conn.commit()
			conn.close()
		except Error as e:
			print(e)

	def updateBook(self,book):
		#result = False
		try:
			id = book.getId()
			book_name = book.getBookName()
			book_genre = book.getBookGenre()
			book_writer = book.getBookWriter()
			book_rating = book.getBookRating()

			conn = sqlite3.connect('db.sqlite3')

			sql = """UPDATE main.myapp_book SET book_name=?, book_genre=?, book_writer=?, book_rating=? WHERE id =?"""
			value = (book_name, book_genre, book_writer, book_rating, id)
			cur =  conn.cursor()
			cur.execute(sql, value)
			conn.commit()
			conn.close()
			#result = True
		except Error as e:
			print(e)
			#result = False
		#return result

	def delete(self,book):
		#result = False
		try:
			id = book.getId()
			book_name = book.getBookName()
			book_genre = book.getBookGenre()
			book_writer = book.getBookWriter()
			book_rating = book.getBookRating()

			conn = sqlite3.connect('db.sqlite3')
			sql = """DELETE FROM main.myapp_book WHERE id =?"""
			value = (id,)

			cur = conn.cursor()
			cur.execute(sql,value)
			conn.commit()
			conn.close()
			#result = True
		except Error as e:
			print(e)
			#result = False
		#return result












