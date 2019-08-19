import copy

class FilledList(list):
	def __init__(self,count,value,*args,**kwargs):
		super().__init__()
		#underscore ignores number comming out of range
		for _ in range(count):
			self.append(copy.copy(value))



fl = FilledList(9,2)
print(len(fl))
print(fl)