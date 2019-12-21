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

def long_total(a=None, b=None, books=None):
    if a is None and b is None and books is None:
        return None

    if a is None and b is None and books is not None:
        a = books.pop(0)
        b = books.pop(0)
        return long_total(a,b,books)

    if a is not None and books and books is not None and b is None:
        b = books.pop(0)
        return long_total(a,b,books)

    if a is not None and b is not None and books is not None:
        return long_total(a+b, None, books)

    if a is not None and b is not None and not books:
        return long_total(a+b, None, None)

    if a is not None and b is None and not books or books is None:
        return a

print(long_total(None, None, [b.price for b in BOOKS]))



from operator import add
from functools import reduce

prices = [
    (6.99, 5),
    (2.94, 15),
    (156.99, 2),
    (99.99, 4),
    (1.82, 102)
]

def product_sales(tup):
    return tup[0]*tup[1]

total = reduce(add,list(map(product_sales,prices)))
print(total)
print(list(map(product_sales,prices)))

from operator import add
from functools import reduce

prices = [
    (6.99, 5),
    (2.94, 15),
    (156.99, 2),
    (99.99, 4),
    (1.82, 102)
]

def product_sales(tup):
    return tup[0]*tup[1]

total = reduce(add, map(product_sales, prices))


### LAMBDAS ###

# if we dont want to write a function which only gets used one time then use lambdas

# this lambda takes two inputs and return the stuff after the colons
# unless we are sure a function is only needed once dont use lambdas
total = reduce(lambda x, y: x + y, [b.price for b in BOOKS])
print(total)

long_books = filter(lambda book: book.number_of_pages >= 600, BOOKS)
print(len(list(long_books)))

good_deals = filter(lambda book: book.price <=6, BOOKS)
print(len(list(good_deals)))


### PARTIALS ###

from functools import partial

def mark_down(book, discount):
    book = copy(book)
    book.price = round(book.price-book.price*discount, 2)
    return book


standard = partial(mark_down, discount=.2)
half = partial(mark_down, discount=0.5)

print(BOOKS[0].price)
print(standard(BOOKS[0]).price)
print(BOOKS[0].price)
print(half(BOOKS[0]).price)

# make long books half price
half_price_books = map(half, filter(is_long_book, BOOKS))
print(list(half_price_books))

### CURRYING ###
# WTF didnt even write this part down

def curried_f(x, y=None, z=None):
    def f(x,y,z):
        return x**3 + y**2 + z
    if y is not None and z is not None:
        return f(x,y,z)

