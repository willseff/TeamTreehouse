class NumString:
	def __init__(self,value):
		self.value = str(value)

	def __str__(self):
		return self.value

	def __int__(self):
		return int(self.value)

	def __float__(self):
		return float(self.value)

#only for plus on right hand side of object need other method for left hand side
	def __add__ (self,other):
		if '.' in self.value:
			return float(self) + other
		return int(self)+other
#stands for refleted add not right add
	def __radd__(self,other):
		return self + other
	#method for inplace add
	def __iadd__(self,other):
		self.value=self + other
		return self.value

	def __mul__(self,other):
		if '.' in self.value:
			return float(self) * other
		return int(self) * other

	def __rmul__(self,other):
		return self*other

five = NumString(5)
print(five + 4)
print(NumString(4.23423)+23)
print(32+NumString(2.2))
age = NumString(25)
age+=1
print(age)
print(NumString(5)*10)
print(10*NumString(12))