#create a new empty list named shopping list
shopping_list=[]

#create a new function named add_to_list that declares a parameter named item
	#add the item to the list

def add_to_list(item):
	shopping_list.append(item)
	# notify the user that item was added and state the number of items in the list currenty
	print('Item was added, there are now {} items in the list'.format(len(shopping_list)))

def show_help():
	print('what shoud we pick up at the store')
	print("""
		Enter "DONE" to stop adding items.
		Enter "HELP" for this help
		ENTER "PRINT" to see the list
		""")

#define a funstion named show list that prints all the items
def show_list():
	print(shopping_list)

show_help()
#infinite loop
while True:
	new_item = input(">")
	if new_item == 'DONE':
		break

	elif(new_item == "HELP"):
		show_help()
		continue
	elif(new_item =="PRINT"):
		show_list()
		continue

	#call add to list wiht new_item as an arguement
	add_to_list(new_item)

show_list()
