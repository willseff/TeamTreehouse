class RaceCar:
    def __init__ (self,color,fuel_remaining,**kwargs):
        self.color = color
        self.fuel_remaining = fuel_remaining
        
        for key, value in kwargs.items():
            setattr(self,key,value)


class Fruit:
	def __init__ (self,has_pulp):
		self.has_pulp= has_pulp

class Orange(Fruit):
    has_pulp = True

    def squeeze(self):
        return self.has_pulp


instance=Orange(has_pulp =False)
print(instance.squeeze())

class Inventory:
    def __init__(self):
        self.slots = []

    def add_item(self, item):
        self.slots.append(item)

class SortedInventory(Inventory):
        
    def add_item(self,item):
        self.slots.append(item)
        self.slots = self.slots.sort()

inv = SortedInventory()
inv.add_item('item')
inv.add_item('hello')

print(inv.slots)

                