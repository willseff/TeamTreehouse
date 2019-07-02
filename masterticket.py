TICKET_PRICE = 10

tickets_remaining = 100

#output how many ticket are remaining using the tickets_remaining variable

print("There are {} tickets remaining".format(tickets_remaining))


#gather the user name and assign it to a new variable

user_name = input("What is your name?   ")

#prompt the user by name and ask how many tickets the would like
number_of_tickets = input("Hello {} how many tickets would you like".format(user_name))
number_of_tickets = int(number_of_tickets)

#caculate the price(number of tickets multiplied by the price) and assign it to a variable

price = number_of_tickets* TICKET_PRICE

# output the price to the screen
print ("The total price is ${} ".format(price))

#prompt user if they want to proceed
prompt = input("would you want to proceed y/n")

	# print out the screen "SOLD!" to confirm purchase
if (prompt == y):


	# and then decrement the tickets remaining by the number of tickets purchased

#Otherwise...

	#thank them by name

