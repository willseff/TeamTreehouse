TICKET_PRICE = 10
SERVICE_CHARGE = 2
tickets_remaining = 100

#calculate price function
def calculate_price(numTicket):
	return TICKET_PRICE * numTicket + SERVICE_CHARGE

while tickets_remaining:

	#output how many ticket are remaining using the tickets_remaining variable

	print("There are {} tickets remaining".format(tickets_remaining))


	#gather the user name and assign it to a new variable

	user_name = input("What is your name?   ")

	#prompt the user by name and ask how many tickets the would like
	number_of_tickets = input("Hello {} how many tickets would you like. ".format(user_name))
	try:
		number_of_tickets = int(number_of_tickets)
		if(number_of_tickets > tickets_remaining):
			raise ValueError("There are only {} tickets left".format(tickets_remaining))
	except ValueError as err:
		print("Sorry an error occured {} Please try again".format(err))

	else:

		#caculate the price(number of tickets multiplied by the price) and assign it to a variable

		price = calculate_price(number_of_tickets)

		# output the price to the screen
		print ("The total price is ${} ".format(price))

		#prompt user if they want to proceed
		prompt = input("would you want to proceed y/n  ")

			# print out the screen "SOLD!" to confirm purchase
		if (prompt == "y"): 
			print("SOLD!")

			# and then decrement the tickets remaining by the number of tickets purchased
			tickets_remaining = tickets_remaining - number_of_tickets 

		#Otherwise...

			#thank them by name
		else:
			print("Thank you {}".format(user_name))


print("Sorry all tickets are sold out")

