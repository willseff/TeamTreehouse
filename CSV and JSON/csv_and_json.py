import csv

with open('museum.csv', newline='') as csvfile:
	artreader = csv.reader(csvfile, delimiter='|')
	rows = list(artreader)
	for row in rows[1:3]:
		print(row, '\n')

with open('museum.csv', newline='') as csvfile:
	#dict reader creates dictionary with column headers to make accessing columns easier
	artreader = csv.DictReader(csvfile, delimiter='|')
	rows = list(artreader)
	for row in rows[1:3]:
		print(row, '\n')
	# print just the values of one column
	for row in rows[1:3]:
		print(row['ManuCountry'])
