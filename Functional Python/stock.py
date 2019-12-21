import json
from copy import copy
from operator import attrgetter, itemgetter

class Book:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return str(self)
    
    
def get_books(filename, raw=False):
    try:
        data = json.load(open(filename))
    except FileNotFoundError:
        return []
    else:
        if raw:
            return data['books']
        return [Book(**book) for book in data['books']]
    
BOOKS = get_books('books.json')
# this is a list of dictionaries
RAW_BOOKS = get_books('books.json', raw=True)

important_list = [5,3,1,2,4]
#important_list.sort() #Bad idea, sorts list in place

# so how to sort important list??
print(important_list) 
print(sorted(important_list)) # this sorts a copy of the list
print(important_list)

# key is a kwarg to sorted that tells what to sort by
pub_sort = sorted(RAW_BOOKS, key=itemgetter('publish_date'))
print(pub_sort[0]['publish_date'], pub_sort[-1]['publish_date'])

# note that the sorted function sends the object to the attrgetter/ itemgetter function
pages_sort = sorted(BOOKS, key=attrgetter('number_of_pages'))
print(pages_sort[0].number_of_pages, pages_sort[-1].number_of_pages)

# map function applies the function to every item in an iterable
a = [1,2,3]
def double(n):
    return n*2

print(list(map(double,a)))

def sales_price(book):
    """ Apply 20% discount to books price"""
    # make a copy of the book
    book = copy(book)
    book.price = round(book.price - book.price*0.2, 2)
    return book

sales_books = list(map(sales_price, BOOKS))
print(BOOKS[0].price)
print(sales_books[0].price)

# map is the same as a list comprehension
sales_books2 = [sales_price(book) for book in BOOKS]
print(sales_books2[0].price)

# map is much more nestable than list comprehensions, its easier to read
# if you need to do somthing once then list comprehension is better
# if somehting needs to be used with other stuff then map is better


### FILTER ###

# return somthing truthy
def is_long_book(book):
    """ Does a book have 600 or more pages"""
    return book.number_of_pages >= 600

long_books = list(filter(is_long_book, BOOKS))
print(len(BOOKS))
print(len(long_books))

# do as list com[renshion

long_books = [book for book in BOOKS if book.number_of_pages >= 600]

### CHAINING ###

def has_roland(book):
    return any(['Roland' in subject for subject in book.subjects])

def titlecase(book):
    book = copy(book)
    book.title = book.title.title()
    return book

# chained two maps and filters
print(list(map(titlecase,filter(has_roland, BOOKS))))

def is_good_deal(book):
    return book.price <= 5

# all books less that 5 dollars when on sale, then sort by the new updated cheap price is]
cheap_books = sorted(
    filter(is_good_deal, map(sales_price, BOOKS)),
    key=attrgetter('price'))

print(cheap_books[0].price)


### REDUCE ###
from functools import reduce

def product(x,y):
    return x * y

# reduce is like a for loop that has a outside value
print(reduce(product, [1,2,3,4,5]))

# the below does the same thing as reduce
total = 0
for x in [1,2,3,4,5]:
    # able to write if statements like this too neat!!
    total = total * x if total else x * 1
print(total)

def add_book_prices(book1, book2):
    return book1 + book2

total = reduce(add_book_prices, [b.price for b in BOOKS])
print(total)




