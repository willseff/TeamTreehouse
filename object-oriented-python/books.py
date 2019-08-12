class Book:
	def __init__(self,title,author):
		self.title = title
		self.author = author

	def __str__(self):
		return ' {}  {} '.format(self.title, self.author)

class Bookcase:
	def __init__(self, books=None):
		self.books=books

	@classmethod

	def create_bookcase(cls,book_list):
		books=[]
		for title, author in book_list:
			books.append(Book(title,author))	
		return cls(books)

bc=Bookcase.create_bookcase([('book1','author1'),('book2', 'author2'),('book3','author3')])
print(bc)