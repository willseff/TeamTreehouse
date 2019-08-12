class Character:
	def __init__(self,name,**kwargs):

		for key, value in kwargs.items():
			setattr(self,key,value)

		print('hello')
		self.name = name


class Thief(Character):
	sneaky = True
	name = 'default'

	def __init__(self,name,sneaky=True,**kwargs):

		super().__init__(name)


	def pickpocket(self):
		print("Called by {}".format(self))
		if (self.sneaky == True):
			return bool(random.randint(0,1))
		else:
			return False

kenneth = Thief('kenneth', scars = 'none', fav_weapon ='whip', sneaky=False)
print(kenneth.sneaky)