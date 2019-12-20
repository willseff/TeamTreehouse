from dec import logme

def print_2():
	print(2)

print_2()

print_2 = logme(print_2)
print_2()

# this does the same thing as above!
@logme
def print_4():
	print(4)

print_4()