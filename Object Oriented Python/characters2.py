class Thief:
	sneaky = True
	name = 'default'

	def __init__ (self,name,sneaky=True,**kwargs):
		self.name=name
		self.sneaky=sneaky

		for key, value in kwargs.items():
			setattr(self,key,value)

	def pickpocket(self):
		print("Called by {}".format(self))
		if (self.sneaky == True):
			return bool(random.randint(0,1))
		else:
			return False

kenneth = Thief('kenneth', scars = 'none', fav_weapon ='whip', sneaky=False)
print(kenneth.sneaky)