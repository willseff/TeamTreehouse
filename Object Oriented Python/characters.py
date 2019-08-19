#Remember first letter capital for classes!!
#understanding self. Self has to be used because a method belongs to a class but it is being called on an instance
import random


class Thief:
	sneaky = True

	def pickpocket(self):
		print("Called by {}".format(self))
		if (self.sneaky == True):
			return bool(random.randint(0,1))
		else:
			return False

kenneth = Thief()
#the self tells the pickpocket method to refer to kenneth
print(kenneth.pickpocket())
#same as 
print(Thief.pickpocket(kenneth))




