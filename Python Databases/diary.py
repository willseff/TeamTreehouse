import datetime
from collections import OrderedDict
import sys
import os

from peewee import *

db = SqliteDatabase('diary.db')

class Entry(Model):
	# content
	content = TextField()
	timestamp = DateTimeField(default=datetime.datetime.now)
	# timestamp

	class Meta:
		database = db

def initialize():
	"""Create the database and the table if it doesnt exist"""
	db.connect()
	db.create_tables([Entry], safe=True)

def menu_loop():
	"""Show the menu"""
	choice = None

	while choice != 'q':
		clear()
		print('Enter q to quit')
		for key, value in menu.items():
			# value.__doc__ is the docstring for that function
			print(f"{key}  {value.__doc__}")
		choice = input('Action: ').lower().strip()

		# this is pretty cool, this is now you select the function based on the dictionary value
		# notice the parenthesis after the square brackets, didnt know you could do that wow!
		if choice in menu:
			clear()
			menu[choice]()

def add_entry():
	""" add an entry"""
	print('enter your entry, press ctrl+d when finished')
	data = sys.stdin.read().strip()

	if data: 
		if input("save entry? [Yn]").lower() != 'n':
			Entry.create(content=data)
			print('Saved Successfully!')


def view_entries(search_query=None):
	""" view previous entries"""
	entries = Entry.select().order_by(Entry.timestamp.desc())
	if search_query:
		entries = entries.where(Entry.content.contains(search_query))

	for entry in entries:
		clear()
		timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
		print(timestamp)
		print ('='* len(timestamp))
		print(entry.content)
		print('d to delete entry')
		print('N next entry')
		print('q return to main menu')

		next_action = input('Action: [Nq]'.strip())
		if next_action == 'q': 
			break

		elif next_action == 'd':
			delete_entry(entry)

def search_entries():
	""" search entries for a sting"""
	view_entries(input('Search query: '))


def delete_entry(entry):
	""" delete an entry""" 
	if input('Are you sure [yN]').lower() == 'y':
		entry.delete_instance()
		print('Entry deleted')

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

menu = OrderedDict([('a', add_entry), 
	('v', view_entries),
	('s', search_entries)
	])

if __name__ == '__main__':
	initialize()
	menu_loop()