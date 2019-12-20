# list order should not change
very_important_list = [5,2,3,1]
name = 'Kenneth'

def mutate():
	very_important_list.sort()

# this is bad don't call methods on mutable types because it changes the list value outside of the scope
print(very_important_list)
mutate()
print(very_important_list)

def global_use():
	# global goes out to the global scope and finds variable with this name
	# this will change the name variable at the top with the nae kenneth
	global name
	name = 'James'

print(name)
global_use()
print(name)

# too much going on in this function its no good
# if you have to explain what is happening in a function then it is probably wrong
def long_func():
	import random
	some_nums = random.shuffle(range(5,250))

	for index, num in enumerate(some_nums):
		if num % 3:
			some_nums[index] = num ** 5
		elif num % 7:
			some_nums[index] = num ** 2

	total = sum(some_nums)
	print("The total of the numbers is {}".format(total))
	return some_nums

# dont take in inputs if it is not used
# too complicated
# inflated scopes
def lots_of_inputs(player_1, player_2. score_1, score_2,
	when = None, where=None, teams=False):
	from collections import namedtuple
	player = namedtuple('Player', ['name', 'score'])
	score = namedtuple('Score', ['player1','player2'])
	p1 = player(player_1, score_1)
	p2 = player(player_2, score_2)
	return score(p1,p2)
