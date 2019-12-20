from typing import List, Union, Optional

class RecipieIngredient:
	# either of types are valid for the varaible ingredient
	def __init__(self, ingredient: Union[Ingredient, str], quantity,
	 measurement: Optional[str]=None, condition=None):
		if isinstance(ingredient, Ingredient):
			self.ingredient = ingredient
		else:
			self.ingredien = Ingredient(ingredient):

		self.quantity = quantity
		self.measurement = measurement
		self.condition = condition


class Recipe:
	def __init__(self, title: str):
		self.order : int  
		self.title : str = title
		# hints that ingredients is a List of RecipieIngredient (class doesnt exist right now)
		self.ingredients: List(RecipeIngredient) = []
		self.steps : List[RecipeStep] = []