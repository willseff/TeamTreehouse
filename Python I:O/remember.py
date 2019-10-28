def rememberer(thing):
	# open file
	# 'w' flag for writing or else there will be an error if there is no file
	# w flag deletetes the file first
	# a flag appends so it is better
	file = open("database.txt", "a")
	# write somthign down
	file.write(thing + "\n")
	# close file
	file.close()
	pass

# better way to write fucntion without needing to explicitly close the file, use the with keyword
def better_rememberer(thing):
	# the with means that variable only exists in that block then after that block the variable is closed
	with open("database.txt", "a") as file:
		file.write(thing + "\n")


if __name__ == '__main__':
	rememberer(input("What should I remmeber? "))