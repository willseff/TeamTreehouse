import sys

def better_rememberer(thing):
	# the with means that variable only exists in that block then after that block the variable is closed
	with open("database.txt", "a") as file:
		file.write(thing + "\n")

def show():
	#open file
	with open("database.txt") as file:
		#python treats files as iterables/ files are iterables
		for line in file:
			print(line)
	# print out each line in file
	# close file
	pass

if __name__ == '__main__':
	if sys.argv[1].lower() == '--list':
		show()
	else:
		better_rememberer(' '.join(sys.argv[1:]))