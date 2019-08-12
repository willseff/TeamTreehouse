import random

from characters import Character
from attributes import *


class Thief(Sneaky,Agile,Character):
    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))