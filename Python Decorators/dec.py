# we can have functions inside functions
def outer():
	number = 5

	def inner():
		print(number)

	inner()

# we can also pass a function into a function and use it
def apply(func, x, y):
	return func(x,y)

def add(x,y):
	return x + y

def sub(x,y):
	return x-y

print(apply(add,5,5))
print(apply(sub,2,8))

def close():
	x=5
	def inner():
		print(x)

	return inner

# close() returns a pointer to the inner function and inner prints x which is 5
# closure() is effectively just inner()
closure = close()
closure()


def add_to_five(num):
	def inner():
		print(num + 5)
	return inner

# notice never had to pass 5 to the inner function
# this effectively gives us private variables
fifteen = add_to_five(10)
fifteen()

def logme(func):
	# import logging but we dont want people to have to import logging to use th decorator
	import logging
	logging.basicConfig(level=logging.DEBUG)

	def inner():
		logging.debug('Called {}'.format(func.__name__))
		return func()
	return inner

