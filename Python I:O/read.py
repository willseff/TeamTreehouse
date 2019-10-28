file = open('teachers.txt')

#reads 10 bytes (10 characters)
print(file.read(10))

#reads the entire documents
# reading file remember where you are and starts from there
print(file.read())

#use file.seek to go to a location
print(file.seek(0))
print(file.read(15))

file.seek(0)

#read lines is more useful because it can be used to reac each line
lines = file.readlines()
print(len(lines))

#print each line backward
for line in lines:
	print(line[::-1])