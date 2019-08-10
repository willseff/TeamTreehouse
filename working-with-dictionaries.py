
course = {'teacher': 'Ashley', 'title': 'Introducing Dictionaries', 'level':'Beginner'}
print(course['teacher'])
print(course.keys())
print(course.values())
print(sorted(course.keys()))
print(sorted(course.values()))

#changing values
course['teacher'] = 'treasure'
course['level'] = 'intermediate'
print(sorted(course.values()))
course['stages'] = '2'
print(course)
#delete key value pair
del(course['stages'])
print(course)

for item in course:
	print(item)

#items method retuns tuples of dictionary items
print(course.items())

for key,value in course.items():
	print(key)
	print(value)

#kwargs packs input into a dictionary and *args packs into tuple
def print_teacher(**kwargs):
	for key , value in kwargs.items():
		print(f'{key}: {value}')

print_teacher(name = 'ashley', job = 'instructor', topic = 'python', second_topic = 'javascript')

#unpacking dictionary as keywod arguements into function
#keys have to match the names of the keywords in order to work. will not work if for example 'name' is changed to 'names'
teacher = {
  'name':'Ashley',
  'job':'Instructor',
  'topic':'Python'
}

def print_teacher(name, job, topic):
    print(name)
    print(job)
    print(topic)

print_teacher(**teacher)