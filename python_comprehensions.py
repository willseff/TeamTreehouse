
# without comprensions
# halfing list
nums = range(5,101)
halves = []
for num in nums: 
	halves.append(num/2)

print(halves)

# one line solution using list comprenshions
halves = [num/2 for num in nums]
print(halves)

# fizzbuzz solution

# numbers from 1-100 divisible by three
print([num for num in range(1,101) if num % 3 == 0])

rows = range(4)
cols = range(10)

# looping though two columns
print([(x,y) for y in rows for x in cols])

# dictionary list comprehension
zipper =zip('abcdefghijklmnopqrstuvwxyz', range(1,27))

for item in zip('abcdefghijklmnopqrstuvwxyz', range(1,27)):
	print(item)

{number: letter for letter, number in zipper}

{student: points for student, points in zip(['Kenenth', 'Dave', 'Joy'],['123','456','789'])}

total_nums = range(1,101)
fizzbuzzes = {
	'fizz': [n for n in total_nums if n%3 == 0],
	'buzz' : [n for n in total_nums if n%7 == 0]
}

# curly brackets are a python set, sets have no order
# also sets are unique, no duplicate values
print({round(x/y) for y in range(1,11) for x in range (2,21)})

fizzbuzzes = {key:set(value) for key, value in fizzbuzzes.items()}

fizzbuzzes['fizzbuzz'] = {n for n in fizzbuzzes['fizz'].intersection(fizzbuzzes['buzz'])}

# this gives us the only the number divisible by 7 and 3 between 1 and 100
print(fizzbuzzes['fizzbuzz'])




