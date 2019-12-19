import json

#with open('148.json') as artfile:
	#load turns into a python object
	# in this case a dict
	#art = json.load(artfile)
	#print(art['description'])

# loads takes the strind and turns it into a python object
nums = json.loads('[1,2,3]')

#dumps turns the list into a sting
json.dumps([5,4,3,2,1])

me = {'first name': 'Kenneth', 'last name': 'Love', 'topic': 'Python'}
#this is not valid json below because single quotes
print(str(me))
# this is valid json bc double quotes
print(json.dumps(me))

craig = {'first name': 'craig', 'last name': 'dennis', 'topic': 'java'}

with open('teachers.json', 'a') as teacherfile:
	# dump into teacher file
	json.dump([me,craig], teacherfile)