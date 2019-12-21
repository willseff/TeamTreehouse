import csv

with open('museum.csv', newline='') as csvfile:
	artreader = csv.reader(csvfile, delimiter='|')
	rows = list(artreader)
	for row in rows[:2]:
		print(', '.join(row))

	