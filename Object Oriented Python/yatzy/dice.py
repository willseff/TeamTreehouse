import random

class Die:
	def __init__(self,sides=2,value=0):
		if not sides >=2:
			raise ValueError('Must have at least two sides')
		if not isinstance(sides,int):
			raise ValueError('Sides must be a whole number')

		self.value = value or random.randint(1,sides)

	def __int__(self):
		return self.value
	def __eq__(self,other):
		return int(self) == other
	def __ne__(self,other):
		return int(self) != other
	def __gt__(self,other):
		return int(self) > other
	def __lt__(self,other):
		return int(self) < other
	def __ge__(self,other):
		return int(self) > other or int(self) == other
	def __le__(self,other):
		return int(self) < other or int(self) == other
	def __add__ (self,other):
		return int(self)+other
	def __radd__ (self,other):
		return self+other
	def __repr__ (self):
		return str(self.value)

#d=Die(value=4)
#print(d.value)

class D6(Die):
	def __init__ (self,value=0):
		super().__init__(sides = 6,value=value)

class Dx(Die):
	def __init__(self,sides=6,value = 0):
		super().__init__(sides = sides,value=value)


#print(D6().value)

#print(int(Dx(sides=100,value=10)))
